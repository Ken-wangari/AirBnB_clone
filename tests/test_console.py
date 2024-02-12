import os
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from parameterized import parameterized

class TestHBNBCommand_create(unittest.TestCase):
    """Unittests for testing create from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        os.remove("file.json")
        os.rename("tmp", "file.json")

    def test_create_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_syntax(self):
        correct = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())
        correct = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())

    @parameterized.expand([
        ("BaseModel",),
        ("User",),
        ("State",),
        ("City",),
        ("Amenity",),
        ("Place",),
        ("Review",)
    ])
    def test_create_object(self, class_name):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
            output_value = output.getvalue().strip()
            self.assertGreater(len(output_value), 0)
            test_key = f"{class_name}.{output_value}"
            self.assertIn(test_key, storage.all().keys())

import os
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from parameterized import parameterized

class TestHBNBCommand_show(unittest.TestCase):
    """Unittests for testing show from the HBNB command interpreter"""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        os.remove("file.json")
        os.rename("tmp", "file.json")

    def test_show_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_missing_id_space_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        # ... (similar tests for other classes)

    def test_show_missing_id_dot_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        # ... (similar tests for other classes)

    def test_show_no_instance_found_space_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())
        # ... (similar tests for other classes)

    def test_show_no_instance_found_dot_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        # ... (similar tests for other classes)

    @parameterized.expand([
        ("BaseModel",),
        ("User",),
        ("State",),
        ("City",),
        ("Amenity",),
        ("Place",),
        ("Review",)
    ])
    def test_show_objects_dot_notation(self, class_name):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"{class_name}.{test_id}"]
            command = f"{class_name}.show({test_id})"
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        # ... (similar tests for other classes)

import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestHBNBCommandDestroy(unittest.TestCase):
    """Unittests for testing destroy from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        storage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        storage.reload()

    def test_destroy_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    # Add more test methods as needed...

if __name__ == "__main__":
    unittest.main()


import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestHBNBCommandAll(unittest.TestCase):
    """Unittests for testing all of the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        storage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_all_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.all()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_all_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    # Add more test methods as needed...

if __name__ == "__main__":
    unittest.main()

import os
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO

class TestHBNBCommandUpdate(unittest.TestCase):
    """Unit tests for testing update from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def setUp(self):
        self.console = HBNBCommand()
        self.console.storage = FileStorage()

    def test_update_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("update"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("update MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_id(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("update BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_id(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("update BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_name(self):
        correct = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("create BaseModel"))
            test_id = output.getvalue().strip()
            test_cmd = "update BaseModel {}".format(test_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_value(self):
        correct = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("create BaseModel"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_cmd = "update BaseModel {} name".format(test_id)
            self.assertFalse(self.console.onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())

if __name__ == "__main__":
    unittest.main()

from unittest.mock import patch, MagicMock
from io import StringIO
import unittest

class TestUpdateCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.mock_storage = MagicMock()
        self.console._storage = self.mock_storage

    def test_update_valid_string_attr_space_notation(self):
        classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
        attributes = ["attr_name", "max_guest", "latitude"]

        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.console.onecmd(f"create {class_name}")
                obj_id = output.getvalue().strip()

            for attr in attributes:
                test_cmd = f"update {class_name} {obj_id} {attr} 'attr_value'"
                self.assertFalse(self.console.onecmd(test_cmd))
                test_dict = self.mock_storage.all()[f"{class_name}.{obj_id}"].__dict__
                self.assertEqual("attr_value", test_dict[attr])

    def test_update_valid_string_attr_dot_notation(self):
        classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
        attributes = ["attr_name", "max_guest", "latitude"]

        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.console.onecmd(f"create {class_name}")
                obj_id = output.getvalue().strip()

            for attr in attributes:
                test_cmd = f"{class_name}.update({obj_id}, {attr}, 'attr_value')"
                self.assertFalse(self.console.onecmd(test_cmd))
                test_dict = self.mock_storage.all()[f"{class_name}.{obj_id}"].__dict__
                self.assertEqual("attr_value", test_dict[attr])

    # Add other test methods for different attribute types and update scenarios

if __name__ == "__main__":
    unittest.main()


import os
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO

class TestHBNBCommandCount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_storage = MagicMock()
        cls.console = HBNBCommand()
        cls.console._storage = cls.mock_storage

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass
        self.mock_storage.reset_mock()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_count_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("MyModel.count()"))
            self.assertEqual("0", output.getvalue().strip())

    def test_count_object(self):
        classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(self.console.onecmd(f"create {class_name}"))
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(self.console.onecmd(f"{class_name}.count()"))
                self.assertEqual("1", output.getvalue().strip())

if __name__ == "__main__":
    unittest.main()

