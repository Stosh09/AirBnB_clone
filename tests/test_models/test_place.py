#!/usr/bin/python3
"""
Module for testing the Place class
"""

import json
import os
import unittest
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.place import Place


class testPlace(unittest.TestCase):
    """
    Defines the test methods to test the Place class
    """

    def setUp(self):
        """
        Set up the necessary environment for each
        test case in the testPlace class.

        This method removes the "file.json"
        file if it exists before each test.

        Inputs:
        - None

        Flow:
        1. Check if the "file.json" file exists.
        2. If it exists, remove the "file.json" file.

        Outputs:
        - None
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """
        Clean up the environment after each
        test case in the testPlace class.

        This method removes the "file.json"
        file if it exists.
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_place_created(self):
        """
        Test whether a Place object is successfully created.

        Example Usage:
        place = Place()
        self.assertTrue(place)

        Inputs: None
        Flow:
        1. Create a new instance of the Place
        class using the default constructor.
        2. Use the assertTrue assertion to check
        if the place object is truthy.

        Outputs: None
        """

        self.assertTrue(Place())

    def test_place_attributes(self):
        """
        Test whether a Place object has
        all the required attributes.

        Example Usage:
        place_1 = Place()
        self.assertTrue(hasattr(place_1, "name"))
        self.assertTrue(hasattr(place_1, "id"))
        self.assertTrue(hasattr(place_1, "created_at"))
        self.assertTrue(hasattr(place_1, "updated_at"))
        self.assertTrue(hasattr(place_1, "user_id"))
        self.assertTrue(hasattr(place_1, "description"))
        self.assertTrue(hasattr(place_1, "number_rooms"))
        self.assertTrue(hasattr(place_1, "number_bathrooms"))
        self.assertTrue(hasattr(place_1, "max_guest"))
        self.assertTrue(hasattr(place_1, "price_by_night"))
        self.assertTrue(hasattr(place_1, "latitude"))
        self.assertTrue(hasattr(place_1, "longitude"))
        self.assertTrue(hasattr(place_1, "amenity_ids"))
        """

        place_1 = Place()

        self.assertTrue(hasattr(place_1, "name"))
        self.assertTrue(hasattr(place_1, "id"))
        self.assertTrue(hasattr(place_1, "created_at"))
        self.assertTrue(hasattr(place_1, "updated_at"))
        self.assertTrue(hasattr(place_1, "user_id"))
        self.assertTrue(hasattr(place_1, "description"))
        self.assertTrue(hasattr(place_1, "number_rooms"))
        self.assertTrue(hasattr(place_1, "number_bathrooms"))
        self.assertTrue(hasattr(place_1, "max_guest"))
        self.assertTrue(hasattr(place_1, "price_by_night"))
        self.assertTrue(hasattr(place_1, "latitude"))
        self.assertTrue(hasattr(place_1, "longitude"))
        self.assertTrue(hasattr(place_1, "amenity_ids"))

    def test_place_id_type(self):
        """
        Test whether the id attribute of a
        Place object is of type string.

        Example Usage:
        place_1 = Place()
        self.assertIsInstance(place_1.id, str)

        Inputs: None
        Flow:
        1. Create a new instance of the Place
        class using the default constructor.
        2. Use the assertIsInstance assertion to
        check if the id attribute of the place_1 object is of type string.

        Outputs: None
        """

        place_1 = Place()
        self.assertIsInstance(place_1.id, str)

    def test_place_id_values(self):
        """
        Test whether the id attribute of two different
        Place objects are not equal.

        Example Usage:
        place_1 = Place()
        place_2 = Place()
        self.assertIsNotNone(place_1.id)
        self.assertIsNotNone(place_2.id)
        self.assertNotEqual(place_1.id, place_2.id)
        """

        place_1 = Place()
        place_2 = Place()
        self.assertIsNotNone(place_1.id)
        self.assertIsNotNone(place_2.id)
        self.assertNotEqual(place_1.id, place_2.id)

    def test_place_class_doc(self):
        """
        Test whether the Place class has a docstring and
        whether the __init__ method of the Place class has a docstring.

        Inputs:
        - None

        Outputs:
        - None
        """
        self.assertGreater(len(Place.__doc__), 3)
        self.assertGreater(len(Place.__init__.__doc__), 3)

    def test_place_name(self):
        """
        Test the attributes of a Place object.

        This method checks the attributes of a Place object,
        such as name, user_id, city_id, description,
        number_bathrooms, number_rooms, max_guest, price_by_night,
        latitude, longitude, and amenity_ids. It also
        verifies the initial values of these attributes and their types.

        Example Usage:
        place_1 = Place()
        assert isinstance(place_1.name, str)
        assert isinstance(place_1.user_id, str)
        assert isinstance(place_1.city_id, str)
        assert isinstance(place_1.description, str)
        assert isinstance(place_1.number_bathrooms, int)
        assert isinstance(place_1.number_rooms, int)
        assert isinstance(place_1.max_guest, int)
        assert isinstance(place_1.price_by_night, int)
        assert isinstance(place_1.latitude, float)
        assert isinstance(place_1.longitude, float)
        assert isinstance(place_1.amenity_ids, list)
        assert place_1.name == ""
        assert place_1.user_id == ""
        assert place_1.city_id == ""
        assert place_1.description == ""
        assert place_1.number_bathrooms == 0
        assert place_1.number_rooms == 0
        assert place_1.price_by_night == 0
        assert place_1.max_guest == 0
        assert place_1.longitude == 0.0
        assert place_1.latitude == 0.0
        assert place_1.amenity_ids == []
        place_1.name = "Nairobi"
        assert place_1.name == "Nairobi"
        """

        place_1 = Place()
        self.assertIsInstance(place_1.name, str)
        self.assertIsInstance(place_1.user_id, str)
        self.assertIsInstance(place_1.city_id, str)
        self.assertIsInstance(place_1.description, str)
        self.assertIsInstance(place_1.number_bathrooms, int)
        self.assertIsInstance(place_1.number_rooms, int)
        self.assertIsInstance(place_1.max_guest, int)
        self.assertIsInstance(place_1.price_by_night, int)
        self.assertIsInstance(place_1.latitude, float)
        self.assertIsInstance(place_1.longitude, float)
        self.assertIsInstance(place_1.amenity_ids, list)
        self.assertEqual(place_1.name, "")
        self.assertEqual(place_1.user_id, "")
        self.assertEqual(place_1.city_id, "")
        self.assertEqual(place_1.description, "")
        self.assertEqual(place_1.number_bathrooms, 0)
        self.assertEqual(place_1.number_rooms, 0)
        self.assertEqual(place_1.price_by_night, 0)
        self.assertEqual(place_1.max_guest, 0)
        self.assertEqual(place_1.longitude, 0.0)
        self.assertEqual(place_1.latitude, 0.0)
        self.assertEqual(place_1.amenity_ids, [])
        place_1.name = "Nairobi"
        self.assertTrue(place_1.name, "Nairobi")

    def test_place_created_updated_at(self):
        """
        Test whether the created_at and updated_at attributes
        of a Place object are instances of the datetime class.

        Inputs:
        - None

        Outputs:
        - None
        """
        place1 = Place()
        self.assertIsInstance(place1.created_at, datetime)
        self.assertIsInstance(place1.updated_at, datetime)

    def test_place_save_updated_at(self):
        """
        Test whether the updated_at attribute of a Place
        object is updated when the save method is called.

        Example Usage:
        place = Place()
        prev_update = place.updated_at
        place.save()
        assert place.updated_at != prev_update

        Inputs: None
        Outputs: None
        """
        place = Place()
        prev_update = place.updated_at
        place.save()
        self.assertNotEqual(place.updated_at, prev_update)

    def test_place_to_dict(self):
        """
        Test the to_dict method of the Place class.

        This method checks if the to_dict method returns a
        dictionary, if the dictionary contains the required
        attributes,and if the dictionary does not
        contain an attribute that was not set.

        Example Usage:
        place = Place()
        place_dict = place.to_dict()
        assert isinstance(place_dict, dict)
        assert place_dict["__class__"] == "Place"
        assert "id" in place_dict
        assert "created_at" in place_dict
        assert "updated_at" in place_dict
        assert "name" not in place_dict
        place.name = "nairobi"
        place_dict = place.to_dict()
        assert "name" in place_dict
        """

        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertIn("id", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)
        self.assertNotIn("name", place_dict)
        place.name = "nairobi"
        place_dict = place.to_dict()
        self.assertIn("name", place_dict)

    def test_place_save_to_file(self):
        """
        Test whether the save method of the Place class
        successfully saves the object to a file.

        Example Usage:
        place = Place()
        place.save()
        assert os.path.exists("file.json") == True

        Inputs: None
        Flow:
        1. Create an instance of the Place class.
        2. Call the save method on the place object.
        3. Use the os.path.exists function to check if
        the "file.json" file exists.

        Outputs: None
        """

        place = Place()
        place.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_place_reload_from_file(self):
        """
        Test whether the reload method of the FileStorage
        class successfully reloads the objects from the file
        and whether the reloaded objects contain the expected object.
        """
        place = Place()
        file = FileStorage()
        place.save()
        place_id = place.id

        file.reload()
        objs = file.all()

        self.assertIn("Place." + place_id, objs.keys())

    def test_place_str_(self):
        """
        Test the __str__ method of the Place class.

        This method creates an instance of the Place class and
        tests if the __str__ method returns the expected string
        representation of the object.

        Example Usage:
        place = Place()
        expected_str = "[Place] ({}) {}".format(place.id, place.__dict__)
        assert str(place) == expected_str

        Inputs:
        - None

        Outputs:
        - None
        """

        place = Place()
        expected_str = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(str(place), expected_str)

    def test_place_update_attributes(self):
        """
        Test whether the 'name' attribute of a 'Place' object can be
        successfully updated and saved to the file storage.

        Example Usage:
        place = Place()
        place.name = 'nairobi'
        place.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_place = new_storage.all()['Place.{}'.format(place.id)]
        assert loaded_place.name == 'nairobi'
        """

        place = Place()
        place.name = 'nairobi'
        place.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_place = new_storage.all()['Place.{}'.format(place.id)]
        self.assertEqual(loaded_place.name, 'nairobi')

    def test_saving_and_loading(self):
        """
        Test whether the save and reload methods of the FileStorage
        class successfully save and reload objects from a file.

        Inputs:
        - None

        Outputs:
        - None
        """

        place = Place()
        place_id = place.id
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_place = new_storage.all()['Place.{}'.format(place_id)]
        self.assertIsInstance(loaded_place, Place)


if __name__ == "__main__":
    unittest.main()
