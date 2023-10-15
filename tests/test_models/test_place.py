#!/usr/bin/python3
"""
Module for testing the Place class
"""

import json
import os
import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
from models.place import Place


class testPlace(unittest.TestCase):
    """
    Defines the test methods for testing the Place class
    """
    def set_up(self):
        """
        Sets up the initial conditions for the test case.

        This method checks if a file named "file.json"
        exists and removes it if it does.

        Parameters:
        - self: The object instance.

        Returns:
        - None
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tear_down(self):
        """
        Remove the "file.json" file if it exists.

        :return: None
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_place_created(self):
        """
        Test if an instance of the Place class
        can be created successfully.

        :param self: The testPlace object.
        :return: None
        """
        self.assertTrue(Place())

    def test_place_attributes(self):
        """
        Test if a Place object has all the required attributes.

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
        Check if the 'id' attribute of a 'Place' object is of type string.

        :param self: The 'testPlace' class instance.
        :return: None

        Example Usage:
        place_1 = Place()
        self.assertIsInstance(place_1.id, str)

        In this example, a 'Place' object is created
        and assigned to the variable 'place_1'.
        The 'test_place_id_type' method is then called
        with 'place_1' as the object to be tested. T
        he method checks if the 'id' attribute of 'place_1'
        is an instance of the 'str' class. I
        f the assertion passes, it means
        that the 'id' attribute is of type string.
        """
        place_1 = Place()
        self.assertIsInstance(place_1.id, str)

    def test_place_id_values(self):
        """
        Test if the id attribute of two different instances
        of the Place class are not equal.

        Inputs:
        - None

        Outputs:
        - None
        """
        place_1 = Place()
        place_2 = Place()
        self.assertIsNotNone(place_1.id)
        self.assertIsNotNone(place_2.id)
        self.assertNotEqual(place_1.id, place_2.id)

    def test_place_class_doc(self):
        """
        Test if the Place class has a docstring and if
        the __init__ method of the Place class has a docstring.

        Inputs:
        - None

        Flow:
        1. Check if the length of the __doc__ attribute of
        the Place class is greater than 3.
        2. Check if the length of the __doc__ attribute of
        the __init__ method of the Place class is greater than 3.

        Outputs:
        - None
        """
        self.assertGreater(len(Place.__doc__), 3)
        self.assertGreater(len(Place.__init__.__doc__), 3)

    def test_place_name(self):
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
        Test if the created_at and updated_at attributes of
        a Place object are instances of the datetime class.

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
        Test whether the updated_at attribute of a
        Place object is updated correctly when the save method is called.

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

        This method checks if the to_dict method returns a dictionary,
        if the dictionary contains the required attributes,
        and if the dictionary does not contain
        an attribute that was not set.
        It also tests if the name attribute is
        included in the dictionary after it is set.

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
        correctly saves the object to a file.

        Example Usage:
        place = Place()
        place.save()
        assert os.path.exists("file.json") == True

        Inputs: None
        Outputs: None
        """

        place = Place()
        place.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_place_reload_from_file(self):
        """
        Test whether the reload method of the FileStorage class
        correctly reloads and deserializes objects
        from a JSON file into the __objects dictionary attribute.
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

        This method checks if the string representation of a
        Place object matches the expected format.

        Example Usage:
        place = Place()
        expected_str = "[Place] ({}) {}".format(place.id, place.__dict__)
        assert str(place) == expected_str

        Inputs: None
        Outputs: None
        """

        place = Place()
        expected_str = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(str(place), expected_str)

    def test_place_update_attributes(self):
        """
        Test the functionality of updating attributes of a Place object.

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
        Test the functionality of saving and loading a
        Place object using the FileStorage class.

        Example Usage:
        place = Place()
        place_id = place.id
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_place = new_storage.all()['Place.{}'.format(place_id)]
        assert isinstance(loaded_place, Place)
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
