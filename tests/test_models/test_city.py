#!/usr/bin/python3
"""
Module for testing the City class
"""
import json
import os
import unittest
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.city import City


class testCity(unittest.TestCase):
    """
    Defines the test methods to test the City class
    """

    def setUp(self):
        """
        Set up the necessary environment for each
        test case in the testCity class.
        Removes the "file.json" file if it exists before each test.
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """
        Clean up the environment after each
        test case in the testCity class.

        This method removes the "file.json"
        file if it exists.

        Example Usage:
        test_city = testCity()
        test_city.tearDown()

        Inputs: None
        Flow:
        1. Check if the "file.json" file exists.
        2. If the file exists, remove it.

        Outputs: None
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_city_created(self):
        """
        Test if a City object is successfully created.

        This method creates a City object and asserts that it is truthy,
        indicating that it was successfully created.

        Inputs:
        None

        Outputs:
        None
        """

        self.assertTrue(City())

    def test_city_attributes(self):
        """
        Test the attributes of the City class.

        This method creates an instance of the
        City class and tests its attributes.

        Example Usage:
        ```python
        test_city_attributes(self)
        ```

        Inputs:
        None

        Outputs:
        None
        """
        city_1 = City()

        self.assertTrue(hasattr(city_1, "name"))
        self.assertTrue(hasattr(city_1, "id"))
        self.assertTrue(hasattr(city_1, "state_id"))
        self.assertTrue(hasattr(city_1, "created_at"))
        self.assertTrue(hasattr(city_1, "updated_at"))

    def test_city_id_type(self):
        """
        Test whether the 'id' attribute of a 'City'
        object is of type string.

        Inputs:
        None

        Flow:
        1. Create a 'City' object named 'city_1'.
        2. Check if the 'id' attribute of 'city_1'
        is an instance of the 'str' class.

        Outputs:
        None
        """
        city_1 = City()
        self.assertIsInstance(city_1.id, str)

    def test_city_id_values(self):
        """
        Test whether the id attribute of two City objects
        are not None and not equal to each other.
        """
        city_1 = City()
        city_2 = City()
        self.assertIsNotNone(city_1.id)
        self.assertIsNotNone(city_2.id)
        self.assertNotEqual(city_1.id, city_2.id)

    def test_city_class_doc(self):
        """
        This method tests whether the `__doc__` attribute of the `City`
        class has a length greater than 3.

        :param self: The object instance
        :return: None
        """
        doc = City.__doc__
        self.assertGreater(len(doc), 3)

    def test_city_name(self):
        """
        Test the name attribute of the City class.

        This method checks if the name attribute is an instance
        of a string, if it is initially an empty string,
        and if it can be successfully updated.

        Example Usage:
        city_1 = City()
        assert isinstance(city_1.name, str)
        assert city_1.name == ""
        city_1.name = "Nairobi"
        assert city_1.name == "Nairobi"
        """

        city_1 = City()
        self.assertIsInstance(city_1.name, str)
        self.assertEqual(city_1.name, "")
        city_1.name = "Nairobi"
        self.assertTrue(city_1.name, "Nairobi")

    def test_city_created_updated_at(self):
        """
        Test whether the created_at and updated_at attributes of a
        City object are instances of the datetime class.

        Inputs:
        None

        Outputs:
        None
        """
        city1 = City()
        self.assertIsInstance(city1.created_at, datetime)
        self.assertIsInstance(city1.updated_at, datetime)

    def test_city_save_updated_at(self):
        """
        Test whether the updated_at attribute of a City object
        is updated when the save method is called.

        Example Usage:
        city = City()
        prev_update = city.updated_at
        city.save()
        assert city.updated_at != prev_update

        Inputs: None
        Outputs: None
        """
        city = City()
        prev_update = city.updated_at
        city.save()
        self.assertNotEqual(city.updated_at, prev_update)

    def test_city_to_dict(self):
        """
        Test the to_dict method of the City class.

        This method checks if the to_dict method returns a dictionary,
        if the dictionary contains the expected keys and values,
        and if the dictionary is updated when the
        name attribute of the City object is changed.

        Example Usage:
        city = City()
        city_dict = city.to_dict()
        assert isinstance(city_dict, dict)
        assert city_dict["__class__"] == "City"
        assert "id" in city_dict
        assert "created_at" in city_dict
        assert "updated_at" in city_dict
        assert "name" not in city_dict

        city.name = "nairobi"
        city_dict = city.to_dict()
        assert "name" in city_dict
        """

        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertNotIn("name", city_dict)
        city.name = "nairobi"
        city_dict = city.to_dict()
        self.assertIn("name", city_dict)

    def test_city_save_to_file(self):
        """
        Test whether the save method of the City class
        successfully saves the object to a file.

        Example Usage:
        city = City()
        city.save()
        assert os.path.exists("file.json") == True

        Inputs: None
        Flow:
        1. Create an instance of the City class named city.
        2. Call the save method on the city object.
        3. Check if the file "file.json" exists.

        Outputs: None
        """

        city = City()
        city.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_city_reload_from_file(self):
        """
        Test whether the reload method of the FileStorage class
        successfully reloads and deserializes objects
        from a JSON file into the __objects dictionary attribute.
        """
        city = City()
        file = FileStorage()
        city.save()
        city_id = city.id

        file.reload()
        objs = file.all()

        self.assertIn("City." + city_id, objs.keys())

    def test_city_str_(self):
        """
        Test the __str__ method of the City class.

        This method creates an instance of the City class and
        tests if the string representation of the object is correct.

        Example Usage:
        city = City()
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        assert str(city) == expected_str

        Inputs: None
        Outputs: None
        """

        city = City()
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)

    def test_city_update_attributes(self):
        """
        Test whether the 'name' attribute of a 'City' object can be
        successfully updated and saved to a file.

        Example Usage:
        city = City()
        city.name = 'nairobi'
        city.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_city = new_storage.all()['City.{}'.format(city.id)]
        assert loaded_city.name == 'nairobi'
        """

        city = City()
        city.name = 'nairobi'
        city.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_city = new_storage.all()['City.{}'.format(city.id)]
        self.assertEqual(loaded_city.name, 'nairobi')

    def test_saving_and_loading(self):
        """
        Test whether the save and reload methods of the
        FileStorage class successfully save and load
        objects to and from a JSON file.

        Inputs:
        None

        Outputs:
        None
        """

        city = City()
        city_id = city.id
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_city = new_storage.all()['City.{}'.format(city_id)]
        self.assertIsInstance(loaded_city, City)


if __name__ == "__main__":
    unittest.main()
