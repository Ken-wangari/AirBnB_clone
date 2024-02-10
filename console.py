#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse_arg(arg):
    """Parse the argument string."""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in arg.split()]
        else:
            lexer = arg[:brackets.span()[0]].split()
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = arg[:curly_braces.span()[0]].split()
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid."""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new class instance and print its id."""
        argl = parse_arg(arg)
        if not argl:
            print("** class name missing **")
        elif argl[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            obj = self.__classes[argl[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Display the string representation of a class instance."""
        argl = parse_arg(arg)
        objdict = storage.all()
        if len(argl) < 2:
            print("** instance id missing **")
        elif argl[0] not in self.__classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Delete a class instance of a given id."""
        argl = parse_arg(arg)
        objdict = storage.all()
        if len(argl) < 2:
            print("** instance id missing **")
        elif argl[0] not in self.__classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Display string representations of all instances."""
        argl = parse_arg(arg)
        objl = [str(obj) for obj in storage.all().values()
                if not argl or obj.__class__.__name__ == argl[0]]
        print(objl)

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""
        argl = parse_arg(arg)
        count = sum(1 for obj in storage.all().values()
                    if obj.__class__.__name__ == argl[0])
        print(count)

    def do_update(self, arg):
        """Update a class instance of a given id."""
        argl = parse_arg(arg)
        objdict = storage.all()
        if len(argl) < 4:
            print("** arguments missing **")
        elif argl[0] not in self.__classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            setattr(obj, argl[2], argl[3])
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

