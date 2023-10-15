#!/usr/bin/python3
"""
Module testing serialization and deserialization module
& File_storage_class
"""

import json
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """
    Test file storage Module
    """

    def set_up(self):
        """
        Remove the "file.json" file if it exists before running each test case.

        Example Usage:
        test_obj = TestFileStorage()
        test_obj.set_up()

        Inputs: None

        Flow:
        1. Check if the "file.json" file exists.
        2. If it exists, remove the file using the `os.remove()` function.

        Outputs: None
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tear_down(self):
        """
        Remove the "file.json" file if it exists before running each test case.

        Inputs:
        - None

        Flow:
        1. Check if the "file.json" file exists.
        2. If it exists, remove the file using the `os.remove()` function.

        Outputs:
        - None
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_private_attr(self):
        """
        Check the presence of private attributes in the FileStorage class.

        Inputs:
        - None

        Outputs:
        - None
        """

        self.assertFalse(hasattr(FileStorage, "__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertFalse(hasattr(FileStorage, "__objects"))

    def test_object_created(self):
        """
        Test whether an object of the FileStorage class
        is created successfully and whether the all
        method returns a dictionary.

        Inputs:
        - None

        Flow:
        1. Create an instance of the FileStorage class.
        2. Assert that the instance is of type FileStorage.
        3. Assert that the all method of the instance returns a dictionary.

        Outputs:
        - None
        """
        file_obj = FileStorage()
        self.assertTrue(file_obj)
        self.assertIsInstance(file_obj.all(), dict)

    def test_save_new_method(self):
        """
        Test the functionality of the 'new' method in the 'FileStorage' class.

        This method creates a new instance of
        the 'BaseModel' class, adds it to the '__objects'
        dictionary in the 'FileStorage' instance,
        and then checks if the object is present in the dictionary.

        Example Usage:
        ```
        base_obj = BaseModel()
        file_obj = FileStorage()
        file_obj.new(base_obj)
        objs = file_obj.all()
        assert base_obj in objs.values()
        ```

        Inputs: None
        Outputs: None
        """

        base_obj = BaseModel()
        file_obj = FileStorage()
        file_obj.new(base_obj)
        objs = file_obj.all()
        self.assertIn(base_obj, objs.values())

    def test_reload(self):
        """
        Test the functionality of the reload
        method in the FileStorage class.

        Example Usage:
        ```
        base_obj = BaseModel()
        file_obj = FileStorage()
        file_obj.new(base_obj)
        file_obj.save()

        new_file = FileStorage()
        new_file.reload()
        objs = new_file.all()
        ```

        Inputs: None

        Flow:
        1. Create a new instance of the BaseModel class.
        2. Create an instance of the FileStorage class.
        3. Add the base_obj to the __objects
        dictionary in the file_obj instance.
        4. Save the file_obj instance to the JSON file.
        5. Create a new instance of the FileStorage class.
        6. Call the reload method on the new_file instance.
        7. Retrieve all objects from the
        new_file instance using the all method.
        8. Store the retrieved objects in the objs variable.

        Outputs:
        - The objs variable contains all the
        objects that were reloaded from the JSON file.
        """
        base_obj = BaseModel()
        file_obj = FileStorage()
        file_obj.new(base_obj)
        file_obj.save()

        new_file = FileStorage()
        new_file.reload()
        objs = new_file.all()
        self.assertTrue(type(objs.values()), BaseModel)

    def test_no_file(self):
        """
        Test whether the reload method in the FileStorage
        class raises a FileNotFoundError when
        the JSON file does not exist.

        Example Usage:
        file_obj = FileStorage()
        try:
            file_obj.reload()
        except FileNotFoundError:
            self.fail("raised FileNotFoundError")
        """
        file_obj = FileStorage()
        try:
            file_obj.reload()
        except FileNotFoundError:
            self.fail("raised FileNotFoundError")

    def test_with_base_model(self):
        """
        Test whether an instance of the BaseModel
        class is successfully saved to the FileStorage object.

        Example Usage:
        base_obj = BaseModel()
        file_obj = FileStorage()
        base_obj.save()

        objs = file_obj.all()
        assert base_obj in objs.values()
        """

        base_obj = BaseModel()
        file_obj = FileStorage()
        base_obj.save()

        objs = file_obj.all()
        self.assertIn(base_obj, objs.values())

    def test_all(self):
        """
        Test the functionality of the all
        method in the FileStorage class.

        Example Usage:
        obj = BaseModel()
        file_obj = FileStorage()
        objects = file_obj.all()
        assert isinstance(objects, dict)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        assert key in objects
        assert objects[key] == obj

        Inputs: None
        Flow:
        1. Create an instance of the BaseModel class.
        2. Create an instance of the FileStorage class.
        3. Call the all method of
        the file_obj instance to retrieve all objects.
        4. Assert that the returned value is of type dict.
        5. Generate the key using the class name and object id.
        6. Assert that the key is present in the objects dictionary.
        7. Assert that the value associated with
        the key in the objects dictionary is equal to the obj instance.

        Outputs: None
        """
        obj = BaseModel()
        file_obj = FileStorage()
        objects = file_obj.all()
        self.assertIsInstance(objects, dict)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, objects)
        self.assertEqual(objects[key], obj)

    def test_save(self):

        obj = BaseModel()
        file_obj = FileStorage()
        file_obj.new(obj)
        file_obj.save()

        self.assertTrue(os.path.exists("file.json"))

        with open("file.json", "r") as f:
            dict_objects = json.load(f)

            self.assertIsInstance(dict_objects, dict)

            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.assertIn(key, dict_objects)
            self.assertEqual(dict_objects[key], obj.to_dict())

    def test_reload_from_empty(self):
        """
        Test the functionality of the reload method
        in the FileStorage class when the JSON file is empty.

        Example Usage:
        file_obj = FileStorage()
        try:
            os.remove("file.json")
        except Exception:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                assert line == "{}"
        assert file_obj.reload() == None

        Inputs: None
        Flow:
        1. Create an instance of the FileStorage class.
        2. Try to remove the "file.json" file if it exists.
        3. Create an empty "file.json" file.
        4. Open the "file.json" file in read mode.
        5. Iterate through each line in the file
        and assert that each line is equal to "{}".
        6. Call the reload method on the file_obj instance.
        7. Assert that the return value of the reload method is None.

        Outputs: None
        """
        file_obj = FileStorage()
        try:
            os.remove("file.json")
        except Exception:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(file_obj.reload(), None)


if __name__ == "__main__":
    unittest.main()
