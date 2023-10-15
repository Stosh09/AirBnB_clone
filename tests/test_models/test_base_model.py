#!/usr/bin/python3
"""
Defines test module for BaseModel class
"""
import json
import unittest
import models
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Test class for BaseModel class module
    """

    def setUp(self):
        """
        Set up the necessary environment for each
        test case in the TestBaseModel class.

        This method checks if a file named "file.json"
        exists and removes it if it does.

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

    def tearDown(self):
        """
        Clean up after each test case in the TestBaseModel class.

        This method checks if a file named "file.json"
        exists and removes it if it does.

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

    def test_obj_created(self):
        """
        Test if an instance of the BaseModel class can be created successfully.

        :param self: The instance of the TestBaseModel class.
        :return: None
        """
        self.assertTrue(BaseModel())

    def test_attributes(self):
        """
        Check if the BaseModel class has the attributes
        id, created_at, and updated_at.

        Example Usage:
        base1 = BaseModel()
        TestBaseModel().test_attributes()

        Inputs: None
        Outputs: None
        """

        base1 = BaseModel()
        self.assertTrue(hasattr(base1, "id"))
        self.assertTrue(hasattr(base1, "created_at"))
        self.assertTrue(hasattr(base1, "updated_at"))

    def test_id_type(self):
        """
        Check if the 'id' attribute of an instance of the
        'BaseModel' class is of type string.

        Inputs:
        - None

        Outputs:
        - None
        """
        base1 = BaseModel()
        self.assertIsInstance(base1.id, str)

    def test_id_values(self):
        """
        Test that the id attribute of two instances of the
        BaseModel class are not equal.

        Inputs:
        - self: an instance of the TestBaseModel class

        Flow:
        1. Two instances of the BaseModel class, base1 and base2, are created.
        2. The id attribute of both instances is
        checked to ensure they are not None.
        3. The id attribute of both instances is
        compared to ensure they are not equal.

        Outputs:
        - None
        """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertIsNotNone(base1.id)
        self.assertIsNotNone(base2.id)
        self.assertNotEqual(base1.id, base2.id)

    def test_class_doc(self):
        """
        This method is a unit test that checks
        if the documentation string (docstring) of the
        BaseModel class is present and has a length greater than 3.

        Example Usage:
        base = BaseModel()
        base.test_class_doc()

        Inputs:
        - None

        Flow:
        1. The test_class_doc method is called on an
        instance of the TestBaseModel class.
        2. The docstring of the BaseModel class is
        assigned to the variable doc.
        3. The length of the doc string is checked to
        ensure it is greater than 3.

        Outputs:
        - None
        """
        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 3)

    def test_function_doc(self):
        """
        This method is a unit test that checks if the documentation
        strings (docstrings) of the __init__, save, to_dict, and __init__
        methods in the BaseModel class and the __init__ method in the
        models module are present and have a length greater than 3.

        Example Usage:
        base = BaseModel()
        base.test_function_doc()

        Inputs: None
        Flow:
        1. The test_function_doc method is called on an instance of the
        TestBaseModel class.
        2. The length of the docstrings of the __init__, save,
        to_dict, and __init__ methods in the BaseModel class and the __init__
        method in the models module are
        checked to ensure they are greater than 3.

        Outputs: None
        """
        self.assertGreater(len(BaseModel.__init__.__doc__), 3)
        self.assertGreater(len(BaseModel.save.__doc__), 3)
        self.assertGreater(len(BaseModel.to_dict.__doc__), 3)
        self.assertGreater(len(models.__init__.__doc__), 3)

    def test_base_created_updated_at(self):
        """
        Test if the 'created_at' and 'updated_at' attributes of an
        instance of the BaseModel class are of type datetime.

        Inputs:
        - None

        Outputs:
        - None
        """
        base1 = BaseModel()
        self.assertIsInstance(base1.created_at, datetime)
        self.assertIsInstance(base1.updated_at, datetime)

    def test_base_save_updated_at(self):
        """
        Test whether the updated_at attribute of an instance of the
        BaseModel class is updated correctly when the save method is called.

        Example Usage:
        base = BaseModel()
        prev_update = base.updated_at
        base.save()
        assert base.updated_at != prev_update

        Inputs: None
        Outputs: None
        """
        base = BaseModel()
        prev_update = base.updated_at
        base.save()
        self.assertNotEqual(base.updated_at, prev_update)

    def test_base_to_dict(self):
        """
        Test the functionality of the to_dict method in the BaseModel class.

        This method checks if the to_dict method returns a
        dictionary representation of the object with the expected attributes.

        Example Usage:
        base = BaseModel()
        base_dict = base.to_dict()
        assert isinstance(base_dict, dict)
        assert base_dict["__class__"] == "BaseModel"
        assert "id" in base_dict
        assert "created_at" in base_dict
        assert "updated_at" in base_dict
        """
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertIn("id", base_dict)
        self.assertIn("created_at", base_dict)
        self.assertIn("updated_at", base_dict)

    def test_base_save_to_file(self):
        """
        Test whether the save method of the BaseModel class
        correctly saves the object to a file.

        Example Usage:
        base = BaseModel()
        base.save()
        assert os.path.exists("file.json") == True

        Inputs: None
        Flow:
        1. Create an instance of the BaseModel class called base.
        2. Call the save method on the base object.
        3. Check if the file "file.json" exists.

        Outputs: None
        """
        base = BaseModel()
        base.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_base_reload_from_file(self):
        """
        Test whether the reload method of the FileStorage class
        correctly loads an object from a file.

        Example Usage:
        base = BaseModel()
        base_model_id = base.id
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_base_model = new_storage.all()['BaseModel.{}'
        .format(base_model_id)]
        assert isinstance(loaded_base_model, BaseModel)
        """
        base = BaseModel()
        base_model_id = base.id
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        loaded_base_model = new_storage.all()['BaseModel.{}'
                                              .format(base_model_id)]
        self.assertIsInstance(loaded_base_model, BaseModel)

    def test_base_str_(self):
        """
        Test the __str__ method of the BaseModel class.

        This method checks if the __str__ method of the BaseModel class
        returns the expected string representation of the object.

        Example Usage:
        base = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(base.id, base.__dict__)
        assert str(base) == expected_str

        Inputs:
        - self: an instance of the TestBaseModel class

        Outputs:
        - None
        """

        base = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(base.id, base.__dict__)
        self.assertEqual(str(base), expected_str)


if __name__ == "__main__":
    unittest.main()
