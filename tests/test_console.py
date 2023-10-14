#!/usr/bin/python3
"""
Defines tests for command interpreter
"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):

    """
    Unittest module for command interpreter
    """
    @classmethod
    def setUpClass(self):
        """
        Set up the necessary environment for running
        the test cases in the TestConsole class.

        This method creates an instance of the HBNBCommand
        class and removes the "file.json" file if it exists.

        Inputs:
        - None

        Outputs:
        - None
        """

        self.command = console.HBNBCommand()
        if os.path.exists("file.json"):
            os.remove("file.json")

    @classmethod
    def tearDownClass(self):
        """
        Clean up the environment after running all
        the test cases in the TestConsole class.

        This method checks if the file "file.json"
        exists and removes it if it does.

        Inputs:
        - None

        Outputs:
        - None
        """

        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_documentation_console(self):
        """
        Test if the documentation for the console module and the
        TestConsole class is present and has a minimum length.

        Inputs:
        - None

        Flow:
        1. Assert that the length of the console module's
        documentation is greater than 3.
        2. Assert that the length of the TestConsole class's
        documentation is greater than 3.

        Outputs:
        - None
        """

        self.assertGreater(len(console.__doc__), 3)
        self.assertGreater(len(self.__doc__), 3)

    def test_emptyline(self):
        """
        Test the behavior of the onecmd method in the HBNBCommand
        class when an empty line is passed as input.

        Example Usage:
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("\n")
            self.assertEqual(fake_output.getvalue(), '')

        Inputs: None
        Outputs: None
        """

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("\n")
            self.assertEqual(fake_output.getvalue(), '')

    def test_create(self):
        """
        Test the behavior of the create command in the HBNBCommand
        class of the console module.

        Example Usage:
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())

        Code Analysis:
        - Inputs: None
        - Flow:
            1. Call the onecmd method of the HBNBCommand
            class with the command "create".
            2. Assert that the output of the command is
            "** class name missing **\n".
        - Outputs: None
        """

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("create MyModel")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("create User")

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("User.all()")
            self.assertEqual('["[User]',
                             fake_output.getvalue()[:8])

    def test_all(self):
        """
        Test the behavior of the 'all' command in the
        HBNBCommand class of the console module.

        Example Usage:
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

        Flow:
        1. Use the 'patch' function from the
        'unittest.mock' module to temporarily replace the
        standard output with a 'StringIO' object.
        2. Call the 'onecmd' method of the 'HBNBCommand'
        class with the command "all MyModel".
        3. Assert that the output of the command is
        "** class doesn't exist **\n".

        Outputs:
        - None
        """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("all City")
            self.assertEqual("[]\n", fake_output.getvalue())

    def test_destroy(self):
        """
        Test the behavior of the destroy command in the
        HBNBCommand class of the console module.

        Example Usage:
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("destroy")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("destroy TheWorld")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("destroy BaseModel 12345 12345")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())
        """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("destroy")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("destroy TheWorld")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("destroy BaseModel 12345 12345")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())

    def test_update(self):
        """
        Test the behavior of the `update` command in the
        `HBNBCommand` class of the console module.

        Example Usage:
        ```python
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("update")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        ```

        Inputs: None
        Flow:
        1. Use the `patch` function from the
        `unittest.mock` module to temporarily replace the
        standard output with a `StringIO` object.
        2. Call the `onecmd` method of the
        `HBNBCommand` class with the command "update".
        3. Assert that the output of the command is
        "** class name missing **\n".

        Outputs: None
        """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("update")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("update MyModel")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("update User")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("update BaseModel 12345")
            self.assertEqual("** attribute name missing **\n",
                             fake_output.getvalue())

    def test_show(self):
        """
        Test the behavior of the `show` command in the
        `HBNBCommand` class of the console module.

        Example Usage:
        ```python
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("show")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        ```

        Code Analysis:
        - Inputs: None
        - Flow:
            1. Use the `patch` function from the `unittest.mock` module to
            temporarily replace the standard output with a `StringIO` object.
            2. Call the `onecmd` method of the
            `HBNBCommand` class with the command "show".
            3. Assert that the output of the command is
            "** class name missing **\n".
        - Outputs: None
        """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("show")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())

    def test_default(self):
        """
        Test the behavior of the `onecmd` method in the
        `HBNBCommand` class when the command "User.count()" is passed as input.

        Example Usage:
        ```python
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("User.count()")
            self.assertEqual(int, type(eval(fake_output.getvalue())))
        ```

        Inputs: None

        Flow:
        1. Use the `patch` function from the `unittest.mock` module to
        temporarily replace the standard output with a `StringIO` object.
        2. Call the `onecmd` method of the `HBNBCommand`
        class with the command "User.count()".
        3. Assert that the output of the command is an integer.

        Outputs: None
        """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("User.count()")
            self.assertEqual(int, type(eval(fake_output.getvalue())))

    def test_pep8_console(self):
        """
        Test the PEP8 compliance of the console.py file.

        Example Usage:
        ```python
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')
        ```

        Inputs: None

        Flow:
        1. Create a `pep8.StyleGuide` object with `quiet=False`
        to enable verbose output.
        2. Initialize the `errors` variable to 0.
        3. Create a list `file` containing the name of the file to be checked,
        in this case, "console.py".
        4. Use the `check_files` method of the `StyleGuide`
        object to check the PEP8 compliance of the file.
        5. Increment the `errors` variable by the total number of errors found.
        6. Assert that the `errors` variable is equal to 0,
        indicating that there are no PEP8 errors in the file.

        Outputs: None
        """
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')

    def test_pep8_test_console(self):
        """
        Pep8 compliance in test_console.py
        """
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["tests/test_console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')


if __name__ == "__main__":
    unittest.main()
