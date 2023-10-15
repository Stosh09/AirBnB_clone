#!/usr/bin/python3
"""
Module that defines class FileStorage
It Serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
from datetime import datetime



class FileStorage:
    """
    Class to perform serialization and deserialization to JSON files.

    Attributes:
        __file_path (str): The path to the JSON file
        where the objects are stored.
        __objects (dict): A dictionary that stores the objects.

    Methods:
        all(self) -> dict:
            Returns a dictionary of objects
            stored in the __objects attribute.

        new(self, obj) -> None:
            Adds a new object to the __objects dictionary attribute.

        save(self) -> None:
            Serializes the objects stored in the __objects
            dictionary attribute into a JSON file.

        reload(self) -> None:
            Reloads and deserializes objects from
            a JSON file into the __objects dictionary attribute.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """
        Returns a dictionary of objects stored in
        the __objects attribute of the FileStorage class.

        Returns:
            dict: A dictionary containing the objects
            stored in the FileStorage instance.
        """
        return self.__objects

    def new(self, obj) -> None:
        """
        Adds a new object to the __objects dictionary attribute.

        Args:
            obj: The object to be added to the __objects dictionary.

        Returns:
            None
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self) -> None:
        """
        Serializes the objects stored in the __objects
        dictionary attribute into a JSON file.

        Returns:
            None
        """
        serial_objects = {}

        for k, v in self.__objects.items():
            serial_objects[k] = v.to_dict()

        with open(self.__file_path, mode='w', encoding="utf-8") as f:
            json.dump(serial_objects, f)

    def reload(self):
        """
        Deserializes objects from a JSON file and stores
        them in the __objects dictionary attribute.

        Inputs:
        - None

        Flow:
        1. Imports the necessary classes from the model files.
        2. Tries to open the JSON file specified by the
        __file_path attribute in read mode.
        3. If the file exists, loads the contents of the
        file into the obj_dict dictionary.
        4. Iterates over each key-value pair in obj_dict.
        5. For each key-value pair, creates an instance of
        the corresponding class using the classes dictionary.
        6. Initializes the instance with the values from the
        dictionary using the **v syntax.
        7. Adds the instance to the __objects dictionary
        with the key as the object ID.
        8. If the file does not exist, does nothing.

        Outputs:
        - None
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
            for k, v in obj_dict.items():
                obj = classes[v["__class__"]](**v)
                self.__objects[k] = obj
        except FileNotFoundError:
            pass
