#!/usr/bin/python3
"""
Defines the BaseModel class
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Defines the BaseModel class.

    Methods:
        __init__(*args, **kwargs): Initializes a new instance of the class.
        __str__(): Generates a string representation of the object.
        save(): Updates the 'updated_at' attribute
        and saves the object to storage.
        to_dict(): Converts the object to a dictionary representation.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable number of positional arguments.
            **kwargs: Variable number of keyword arguments.

        Example Usage:
            obj = BaseModel(arg1, arg2, key1=value1, key2=value2)
            obj = BaseModel()

        Flow:
            1. If kwargs is provided, iterate over each key-value pair.
            2. If the key is "created_at" or "updated_at",
            convert the corresponding value to a datetime object
            using the specified format.
            3. If the key is not "__class__", set the attribute
             of the object with the key as the attribute name
             and the value as the attribute value.
            4. If kwargs is not provided, set the id attribute
            to a new UUID, the created_at attribute
            to the current datetime, and the updated_at attribute
            to the current datetime.
            5. Call the new method of the storage object
            to add the object to storage.

        Returns:
            None
            
        """
        if kwargs:

            for i, j in kwargs.items():

                if i == "created_at" or i == "updated_at":
                    j = datetime.strptime(j, "%Y-%m-%dT%H:%M:%S.%f")

                if i != "__class__":
                    setattr(self, i, j)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object.

        :return: A string representation of the
        object in the format: '[class_name] (object_id) {object_dictionary}'.
        :rtype: str
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute of the
        object to the current datetime and saves the object to storage.

        Inputs:
        - None

        Flow:
        1. The 'save' method is called on an instance of the 'BaseModel' class.
        2. The 'updated_at' attribute of the object is updated
        with the current datetime using 'datetime.now()'.
        3. The 'save' method of the 'storage' object
        is called to save the object to storage.

        Outputs:
        - None
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Convert an instance of the BaseModel class
        into a dictionary representation.

        Returns:
            dict: A dictionary representation of the
            instance with the following keys:
                - '__class__': The name of the class.
                - 'id': The unique identifier of the instance.
                - 'created_at': The creation timestamp of
                the instance in ISO format.
                - 'updated_at': The last update timestamp of
                the instance in ISO format.
        """
        class_dict = {
            "__class__": self.__class__.__name__
        }
        for i, j in self.__dict__.items():

            if i == "created_at":
                class_dict[i] = j.isoformat()

            elif i == "updated_at":
                class_dict[i] = j.isoformat()

            else:
                class_dict[i] = j

        return class_dict
