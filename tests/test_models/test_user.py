#!/usr/bin/python3
"""
Module for testing the User class
"""
import json
import os
import unittest
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.user import User


class testUser(unittest.TestCase):
    """
    Defines the test methods to test the User class
    """

    def setUp(self):
        """
        Set up the necessary environment for each
        test case in the testUser class.

        This method removes the "file.json" file
        if it exists before each test.

        Inputs: None

        Outputs: None
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """
        Clean up the environment after each test case
        in the testUser class.

        This method checks if the file "file.json"
        exists and removes it if it does.

        Example Usage:
        test_user = testUser()
        test_user.tearDown()
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_user_created(self):
        """
        Test if a User object is successfully created.

        This method is a unit test that checks if a User
        object is successfully created.

        Example Usage:
        test_user = testUser()
        test_user.test_user_created()

        Inputs:
        None

        Flow:
        1. Create an instance of the `testUser` class.
        2. Call the `test_user_created` method.
        3. Inside the method, create a User object.
        4. Use the `assertTrue` assertion to check if the
        User object is truthy.

        Outputs:
        None
        """
        self.assertTrue(User())

    def test_attributes(self):
        """
        Test if the User object has the expected attributes.

        Inputs:
        - None

        Flow:
        1. Create an instance of the User class.
        2. Call the test_attributes method.
        3. Inside the method, create a User object.
        4. Use the assertTrue assertion to check if the User object
        has the attributes: "email", "password", "first_name",
        "last_name", "id", "created_at", and "updated_at".

        Outputs:
        - None
        """

        user_1 = User()

        self.assertTrue(hasattr(user_1, "email"))
        self.assertTrue(hasattr(user_1, "password"))
        self.assertTrue(hasattr(user_1, "first_name"))
        self.assertTrue(hasattr(user_1, "last_name"))
        self.assertTrue(hasattr(user_1, "id"))
        self.assertTrue(hasattr(user_1, "created_at"))
        self.assertTrue(hasattr(user_1, "updated_at"))

    def test_user_id_type(self):
        """
        Check if the 'id' attribute of a 'User'
        object is of type string.

        Inputs:
        - None

        Outputs:
        - None
        """

        user_1 = User()
        self.assertIsInstance(user_1.id, str)

    def test_user_id_values(self):
        """
        Test if the id attribute of two different User
        objects are not None and not equal to each other.

        Inputs:
        - None

        Outputs:
        - None
        """
        user_1 = User()
        user_2 = User()
        self.assertIsNotNone(user_1.id)
        self.assertIsNotNone(user_2.id)
        self.assertNotEqual(user_1.id, user_2.id)

    def test_class_doc(self):
        """
        This method is a unit test that checks if the
        User class has a docstring and if the __init__
        method of the User class has a docstring.

        Example Usage:
        test_user = testUser()
        test_user.test_class_doc()

        Inputs:
        - None

        Flow:
        1. Create an instance of the testUser class.
        2. Call the test_class_doc method.
        3. Get the docstring of the User class and assign it
        to the variable doc.
        4. Use the assertGreater assertion to check if the
        length of doc is greater than 3.
        5. Get the docstring of the __init__ method of the
        User class and check if its length is greater than 3.

        Outputs:
        - None
        """
        doc = User.__doc__
        self.assertGreater(len(doc), 3)
        self.assertGreater(len(User.__init__.__doc__), 3)

    def test_user_created_updated_at(self):
        """
        Test if the `created_at` and `updated_at` attributes
        of a `User` object are instances of the `datetime` class.

        Inputs:
        - None

        Outputs:
        - None
        """
        user1 = User()
        self.assertIsInstance(user1.created_at, datetime)
        self.assertIsInstance(user1.updated_at, datetime)

    def test_user_save_updated_at(self):
        """
        Test if the 'updated_at' attribute of a User object
        is updated after calling the save method.

        Inputs:
        - None

        Flow:
        1. Create an instance of the testUser class.
        2. Call the test_user_save_updated_at method.
        3. Inside the method, create a User object.
        4. Get the current value of the updated_at attribute
        and assign it to the variable prev_update.
        5. Call the save method on the User object.
        6. Use the assertNotEqual assertion to check if the
        updated_at attribute of the User object is not equal
        to prev_update.

        Outputs:
        - None
        """
        user = User()
        prev_update = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, prev_update)

    def test_user_to_dict(self):
        """
        Test the to_dict method of the User class.

        This method checks if the to_dict method returns
        a dictionary with the expected attributes and values.

        Inputs:
        - None

        Outputs:
        - None
        """

        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertNotIn("name", user_dict)
        user.name = "betty"
        user_dict = user.to_dict()
        self.assertIn("name", user_dict)

    def test_user_save_to_file(self):
        """
        Test if the save method of the User class successfully
        saves the user object to a file.

        Inputs:
        - None

        Outputs:
        - None
        """

        user = User()
        user.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_user_reload_from_file(self):
        """
        Test if a User object can be successfully
        reloaded from a file.

        This method creates a User object and a FileStorage object.
        It saves the User object to the file, then reloads
        the file using the FileStorage object's reload method.
        It checks if the User object exists in the reloaded file.

        Inputs:
        - None

        Outputs:
        - None
        """

        user = User()
        file = FileStorage()
        user.save()
        user_id = user.id

        file.reload()
        objs = file.all()

        self.assertIn("User." + user_id, objs.keys())

    def test_user_str_(self):
        """
        Test the __str__ method of the User class.

        This method creates a User object and compares
        its string representation with the expected
        string representation.

        Inputs:
        - None

        Outputs:
        - None
        """

        user = User()
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

    def test_user_update_attributes(self):
        """
        Test if the email attribute of a User object
        can be successfully updated and saved to a file.

        Example Usage:
        test_user = testUser()
        test_user.test_user_update_attributes()

        Inputs: None

        Flow:
        1. Create a new instance of the User class and
        assign it to the variable user.
        2. Set the email attribute of user to 'test@example.com'.
        3. Call the save method on user to save the changes to the file.
        4. Create a new instance of the FileStorage class
        and assign it to the variable new_storage.
        5. Call the reload method on new_storage to reload
        the file and update the __objects dictionary.
        6. Get the User object with the corresponding id
        from the __objects dictionary and assign it to the
        variable loaded_user.
        7. Use the assertEqual assertion to check if the
        email attribute of loaded_user is equal to 'test@example.com'.

        Outputs: None
        """
        user = User()
        user.email = 'test@example.com'
        user.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_user = new_storage.all()['User.{}'.format(user.id)]
        self.assertEqual(loaded_user.email, 'test@example.com')

    def test_saving_and_loading(self):
        """
        Tests if a User object can be successfully saved
        to a file and then loaded back from the file.

        Inputs:
        - None

        Outputs:
        - None
        """

        user = User()
        user_id = user.id
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_user = new_storage.all()['User.{}'.format(user_id)]
        self.assertIsInstance(loaded_user, User)

    def test_first_name(self):
        """
        Test if the first_name attribute of a User object
        is of type string and has an initial value of an
        empty string.

        Inputs:
        - None

        Outputs:
        - None
        """
        user = User()
        self.assertIsInstance(user.first_name, str)
        self.assertEqual(user.first_name, "")

    def test_last_name(self):
        """
        Test if the last_name attribute of a User object
        is of type string and has an initial value of an
        empty string.

        Inputs:
        - None

        Outputs:
        - None
        """
        user = User()
        self.assertIsInstance(user.last_name, str)
        self.assertEqual(user.last_name, "")

    def test_email(self):
        """
        Test if the email attribute of a User object is
        of type string and has an initial value of an empty string.

        Inputs:
        - None

        Flow:
        1. Create an instance of the User class and
        assign it to the variable user.
        2. Use the assertIsInstance assertion to
        check if the email attribute of user is of type string.
        3. Use the assertEqual assertion to check if the
        email attribute of user is equal to an empty string.

        Outputs:
        - None
        """
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertEqual(user.email, "")

    def test_password(self):
        """
        Test if the password attribute of a User object
        is of type string and has an initial value of an empty string.

        Inputs: None

        Outputs: None
        """
        user = User()
        self.assertIsInstance(user.password, str)
        self.assertEqual(user.password, "")


if __name__ == "__main__":
    unittest.main()
