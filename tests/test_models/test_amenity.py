#!/usr/bin/python3
"""
Module for testing the Amenity class
"""
# import json
import os
import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Defines the test methods to test Amenity class
    """
    def set_up(self):
        """
        Set up the test environment before running
        ach test case in the TestAmenity class.

        Inputs:
        - None

        Flow:
        1. Check if the file "file.json" exists.
        2. If the file exists, remove it.

        Outputs:
        - None
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tear_down(self):
        """
        Clean up the test environment after running
        each test case in the TestAmenity class.

        :param self: The TestAmenity instance.
        :return: None
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_amenity_created(self):
        """
        Test if an instance of the Amenity
        class can be successfully created.

        Example Usage:
        amenity = Amenity()
        self.assertTrue(amenity)

        Inputs: None
        Flow:
        1. Create an instance of the Amenity class.
        2. Assert that the instance is truthy.

        Outputs: None
        """
        self.assertTrue(Amenity())

    def test_attributes(self):
        """
        Test if an instance of the Amenity
        class has the expected attributes.

        Example Usage:
        amenity_1 = Amenity()
        self.assertTrue(hasattr(amenity_1, "name"))
        self.assertTrue(hasattr(amenity_1, "id"))
        self.assertTrue(hasattr(amenity_1, "created_at"))
        self.assertTrue(hasattr(amenity_1, "updated_at"))

        Inputs: None
        Flow:
        1. Create an instance of the Amenity class.
        2. Use the hasattr function to check
        if the instance has the attributes "name", "id",
        "created_at", and "updated_at".
        3. Assert that all the checks return True.

        Outputs: None
        """
        amenity_1 = Amenity()
        self.assertTrue(hasattr(amenity_1, "name"))
        self.assertTrue(hasattr(amenity_1, "id"))
        self.assertTrue(hasattr(amenity_1, "created_at"))
        self.assertTrue(hasattr(amenity_1, "updated_at"))

    def test_amenity_id_type(self):
        """
        Check if the 'id' attribute of an
        instance of the 'Amenity' class is of type string.

        Example Usage:
        amenity_1 = Amenity()
        self.assertIsInstance(amenity_1.id, str)

        Inputs: None
        Outputs: None
        """
        amenity_1 = Amenity()
        self.assertIsInstance(amenity_1.id, str)

    def test_amenity_id_values(self):
        """
        Test if the id attribute of two instances of
        the Amenity class are not None and not equal to each other.

        Example Usage:
        amenity_1 = Amenity()
        amenity_2 = Amenity()
        self.assertIsNotNone(amenity_1.id)
        self.assertIsNotNone(amenity_2.id)
        self.assertNotEqual(amenity_1.id, amenity_2.id)

        Inputs: None
        Flow:
        1. Create two instances of the Amenity class.
        2. Use the assertIsNotNone method to check
        that the id attribute of both instances is not None.
        3. Use the assertNotEqual method to check
        that the id attribute of both instances is not equal.

        Outputs: None
        """
        amenity_1 = Amenity()
        amenity_2 = Amenity()

        self.assertIsNotNone(amenity_1.id)
        self.assertIsNotNone(amenity_2.id)
        self.assertNotEqual(amenity_1.id, amenity_2.id)

    def test_class_doc(self):
        """
        This method is a unit test that checks if the
        documentation string (`__doc__`) of the `Amenity`
        class is greater than 3 characters.

        Example Usage:
        amenity = Amenity()
        self.assertGreater(len(amenity.__doc__), 3)

        Inputs: None

        Flow:
        1. Create an instance of the `Amenity` class.
        2. Access the `__doc__` attribute of the `Amenity` class.
        3. Get the length of the `__doc__` string.
        4. Use the `assertGreater` method to check
        if the length of the `__doc__` string is greater than 3.

        Outputs: None
        """
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 3)

    def test_amenity_name(self):
        """
        Test the functionality of the `name` attribute in the `Amenity` class.

        Example Usage:
        amenity_1 = Amenity()
        self.assertIsInstance(amenity_1.name, str)
        self.assertEqual(amenity_1.name, "")
        amenity_1.name = "bathroom"
        self.assertTrue(amenity_1.name, "bathroom")
        """

        amenity_1 = Amenity()
        self.assertIsInstance(amenity_1.name, str)
        self.assertEqual(amenity_1.name, "")
        amenity_1.name = "bathroom"
        self.assertTrue(amenity_1.name, "bathroom")

    def test_amenity_created_updated_at(self):
        """
        Test if the created_at and updated_at attributes
        of an instance of the Amenity class are of type datetime.

        Inputs:
        - None

        Outputs:
        - None
        """
        amenity1 = Amenity()
        self.assertIsInstance(amenity1.created_at, datetime)
        self.assertIsInstance(amenity1.updated_at, datetime)

    def test_amenity_save_updated_at(self):
        """
        Test whether the updated_at attribute of an
        instance of the Amenity class is
        updated when the save method is called.

        Example Usage:
        amenity = Amenity()
        prev_update = amenity.updated_at
        amenity.save()
        assert amenity.updated_at != prev_update

        Inputs: None
        Outputs: None
        """
        amenity = Amenity()
        prev_update = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, prev_update)

    def test_amenity_to_dict(self):
        """
        Test the functionality of the to_dict method in the Amenity class.

        This method checks if the to_dict method
        returns a dictionary with the expected attributes and values.

        Example Usage:
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertNotIn("name", amenity_dict)
        amenity.name = "bathroom"
        amenity_dict = amenity.to_dict()
        self.assertIn("name", amenity_dict)
        """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertNotIn("name", amenity_dict)
        amenity.name = "bathroom"
        amenity_dict = amenity.to_dict()
        self.assertIn("name", amenity_dict)

    def test_amenity_save_to_file(self):
        """
        Test the functionality of saving an
        instance of the Amenity class to a file.

        Example Usage:
        amenity = Amenity()
        amenity.save()
        self.assertTrue(os.path.exists("file.json"))

        Inputs: None
        Outputs: None
        """

        amenity = Amenity()
        amenity.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_amenity_reload_from_file(self):
        """
        Test the functionality of reloading and
        deserializing objects from a JSON file into
        the __objects dictionary attribute of the FileStorage class.

        Example Usage:
        amenity = Amenity()
        file = FileStorage()
        amenity.save()
        amenity_id = amenity.id

        file.reload()
        objs = file.all()

        self.assertIn("Amenity." + amenity_id, objs.keys())
        """

        amenity = Amenity()
        file = FileStorage()
        amenity.save()
        amenity_id = amenity.id

        file.reload()
        objs = file.all()

        self.assertIn("Amenity." + amenity_id, objs.keys())

    def test_amenity_str_(self):
        """
        Test the __str__ method of the Amenity class.

        This method checks if the __str__ method of
        the Amenity class returns the expected string
        representation of an instance of the class.

        Example Usage:
        amenity = Amenity()
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)

        Inputs: None
        Outputs: None
        """

        amenity = Amenity()
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)

    def test_amenity_update_attributes(self):
        """
        Test the functionality of updating
        attributes of an instance of the Amenity class.

        Example Usage:
        amenity = Amenity()
        amenity.name = 'nairobi'
        amenity.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_amenity = new_storage.all()['Amenity.{}'.format(amenity.id)]
        self.assertEqual(loaded_amenity.name, 'nairobi')
        """

        amenity = Amenity()
        amenity.name = 'nairobi'
        amenity.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_amenity = new_storage.all()['Amenity.{}'.format(amenity.id)]
        self.assertEqual(loaded_amenity.name, 'nairobi')

    def test_saving_and_loading(self):
        """
        Test the functionality of saving and
        loading an instance of the Amenity
        class using the FileStorage class.

        Example Usage:
        amenity = Amenity()
        amenity_id = amenity.id
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_amenity = new_storage.all()['Amenity.{}'.format(amenity_id)]
        self.assertIsInstance(loaded_amenity, Amenity)
        """

        amenity = Amenity()
        amenity_id = amenity.id
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()

        loaded_amenity = new_storage.all()['Amenity.{}'.format(amenity_id)]
        self.assertIsInstance(loaded_amenity, Amenity)


if __name__ == "__main__":
    unittest.main()
