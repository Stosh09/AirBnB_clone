#!/usr/bin/python3
"""
Module for testing the State class
"""
import json
import os
import unittest
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.state import State


class testState(unittest.TestCase):
    """
    Defines the test methods to test the State class
    """

    def setUp(self):
        """
        Set up the necessary environment for each test
        case in the testState class.

        This method removes the "file.json" file if it
        exists before running each test.

        Inputs:
        - None

        Flow:
        1. Check if the "file.json" file exists.
        2. If it exists, remove the file.

        Outputs:
        - None
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """
        Clean up the environment after each test case.

        This method checks if the "file.json" file
        exists and removes it if it does.

        Inputs:
        - None

        Flow:
        1. Check if the "file.json" file exists.
        2. If it exists, remove the file.

        Outputs:
        - None
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_state_created(self):
        """
        Test if a State object is successfully created.

        Example Usage:
        state = State()
        test_state_created()

        Inputs:
        - None

        Flow:
        1. Create a State object.
        2. Call the `test_state_created` method.
        3. The method asserts that the State object is truthy,
        meaning it was successfully created.

        Outputs:
        - None
        """
        self.assertTrue(State())

    def test_state_attributes(self):
        """
        Test if a State object has the required attributes.

        Inputs:
        - None

        Flow:
        1. Create a State object.
        2. Check if the State object has the attributes
        "name", "id", "created_at", and "updated_at".
        3. Assert that all the attributes are present.

        Outputs:
        - None
        """

        state_1 = State()

        self.assertTrue(hasattr(state_1, "name"))
        self.assertTrue(hasattr(state_1, "id"))
        self.assertTrue(hasattr(state_1, "created_at"))
        self.assertTrue(hasattr(state_1, "updated_at"))

    def test_state_id_type(self):
        """
        Test whether the `id` attribute of a `State`
        object is of type string.

        Example Usage:
        state_1 = State()
        test_state_id_type()

        Inputs:
        - None

        Flow:
        1. Create a `State` object.
        2. Call the `test_state_id_type` method.
        3. Check the type of the `id` attribute of the `State`
        object.
        4. Assert that the `id` attribute is an instance of the
        `str` class.

        Outputs:
        - None
        """
        state_1 = State()
        self.assertIsInstance(state_1.id, str)

    def test_state_id_values(self):
        """
        Test whether the `id` attribute of two `State` objects are unique.

        Example Usage:
        state_1 = State()
        state_2 = State()
        test_state_id_values()

        Inputs: None

        Flow:
        1. Create two `State` objects, `state_1` and `state_2`.
        2. Check if the `id` attribute of both objects is not `None`.
        3. Assert that the `id` attribute of `state_1` is not equal
        to the `id` attribute of `state_2`.

        Outputs: None
        """
        state_1 = State()
        state_2 = State()
        self.assertIsNotNone(state_1.id)
        self.assertIsNotNone(state_2.id)
        self.assertNotEqual(state_1.id, state_2.id)

    def test_state_class_doc(self):
        """
        Test if the State class has a docstring and if the __init__
        method of the State class has a docstring.

        Example Usage:
        state = State()
        test_state_class_doc()

        Inputs:
        - None

        Flow:
        1. Create a State object.
        2. Call the test_state_class_doc method.
        3. Check the length of the __doc__ attribute of the State class.
        4. Check the length of the __doc__ attribute of the __init__
        method of the State class.
        5. Assert that both lengths are greater than 3.

        Outputs:
        - None
        """
        self.assertGreater(len(State.__doc__), 3)
        self.assertGreater(len(State.__init__.__doc__), 3)

    def test_state_name(self):
        """
        Test the behavior of the name attribute of a State object.

        This method creates a State object and tests the
        behavior of its name attribute.

        Inputs:
        - None

        Outputs:
        - None
        """

        state_1 = State()
        self.assertIsInstance(state_1.name, str)
        self.assertEqual(state_1.name, "")
        state_1.name = "Nairobi"
        self.assertTrue(state_1.name, "Nairobi")

    def test_state_created_updated_at(self):
        """
        Test whether the `created_at` and `updated_at`
        attributes of a `State` object are instances of the
        `datetime` class.

        Inputs:
        - None

        Outputs:
        - None
        """
        state1 = State()
        self.assertIsInstance(state1.created_at, datetime)
        self.assertIsInstance(state1.updated_at, datetime)

    def test_state_save_updated_at(self):
        """
        Test whether the updated_at attribute of a State object
        is updated after calling the save method.

        Example Usage:
        state = State()
        prev_update = state.updated_at
        state.save()
        test_state_save_updated_at()

        Inputs: None
        Outputs: None
        """
        state = State()
        prev_update = state.updated_at
        state.save()
        self.assertNotEqual(state.updated_at, prev_update)

    def test_state_to_dict(self):
        """
        Test the to_dict() method of the State class.

        This method checks if the to_dict() method returns a
        dictionary with the expected attributes and values.

        Example Usage:
        state = State()
        state_dict = state.to_dict()
        assert isinstance(state_dict, dict)
        assert state_dict["__class__"] == "State"
        assert "id" in state_dict
        assert "created_at" in state_dict
        assert "updated_at" in state_dict
        assert "name" not in state_dict
        state.name = "nairobi"
        state_dict = state.to_dict()
        assert "name" in state_dict
        """
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertNotIn("name", state_dict)
        state.name = "nairobi"
        state_dict = state.to_dict()
        self.assertIn("name", state_dict)

    def test_state_save_to_file(self):
        """
        Test whether the save method of the State class
        successfully saves the state object to a file.

        Inputs:
        - None

        Flow:
        1. Create a State object.
        2. Call the save method of the State object.
        3. Check if the file "file.json" exists.
        4. Assert that the file exists.

        Outputs:
        - None
        """
        state = State()
        state.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_state_reload_from_file(self):
        """
        Test whether the reload method of the FileStorage
        class successfully reloads and deserializes objects
        from a JSON file into the __objects dictionary attribute.
        """
        state = State()
        file = FileStorage()
        state.save()
        state_id = state.id

        file.reload()
        objs = file.all()

        self.assertIn("State." + state_id, objs.keys())

    def test_state_str_(self):
        """
        Test the behavior of the __str__ method of the State class.

        This method creates a State object and compares
        the string representation of the object
        with an expected string.

        Example Usage:
        state = State()
        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        assert str(state) == expected_str

        Inputs: None
        Outputs: None
        """

        state = State()
        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)

    def test_state_update_attributes(self):
        """
        Test whether the 'name' attribute of a 'State'
        object can be updated and saved correctly.

        Example Usage:
        state = State()
        state.name = 'nairobi'
        state.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_state = new_storage.all()['State.{}'.format(state.id)]
        assert loaded_state.name == 'nairobi'

        Inputs: None
        Flow:
        1. Create a 'State' object.
        2. Set the 'name' attribute of the 'State' object to 'nairobi'.
        3. Save the 'State' object.
        4. Create a new 'FileStorage' object.
        5. Reload the objects from the JSON file into the
        '__objects' dictionary attribute of the 'FileStorage' object.
        6. Retrieve the 'State' object from the '__objects'
        dictionary using its ID.
        7. Assert that the 'name' attribute of the loaded
        'State' object is equal to 'nairobi'.

        Outputs: None
        """
        state = State()
        state.name = 'nairobi'
        state.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_state = new_storage.all()['State.{}'.format(state.id)]
        self.assertEqual(loaded_state.name, 'nairobi')

    def test_saving_and_loading(self):
        """
        Test whether a State object can be saved to a
        file and then successfully loaded from that file.

        Inputs:
        - None

        Outputs:
        - None
        """
        state = State()
        state_id = state.id
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_state = new_storage.all()['State.{}'.format(state_id)]
        self.assertIsInstance(loaded_state, State)


if __name__ == "__main__":
    unittest.main()
