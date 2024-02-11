#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import classes


def parse(arg):
    """Parse the arguments."""
    pattern = r"(\w+)\s?(\(.*\))?"
    match = re.match(pattern, arg)
    if match:
        command = match.group(1)
        args = match.group(2)
        if args:
            args = split(args[1:-1])
        return command, args
    return None, None


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid."""
        command, args = parse(arg)
        if command in ["all", "show", "destroy", "count", "update"]:
            getattr(self, "do_" + command)(*args)
        else:
            print("*** Unknown syntax: {}".format(arg))

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new class instance and print its id."""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Display the string representation of a class instance of a given id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete a class instance of a given id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Display string representations of all instances of a given class."""
        if arg and arg.split()[0] not in classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in storage.all().values() if not arg or obj.__class__.__name__ == arg.split()[0]])

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        print(len([obj for obj in storage.all().values() if obj.__class__.__name__ == class_name]))

    def do_update(self, arg):
        """Update a class instance of a given id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(storage.all()[key], args[2], args[3])
        storage.all()[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

