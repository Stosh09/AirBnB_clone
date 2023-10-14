#!/usr/bin/python3
"""
Defines the BaeModel class
Parent to all classes
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
        save(): Updates the 'updated_at' attribute and saves the object to storage.
        to_dict(): Converts the object to a dictionary representation.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        If it is a new instance (not from a dictionary representation),
        add a call to the method new(self) on storage.

        Args:
            *args: Variable arguments.
            **kwargs: Keyword arguments.

        Returns:
            BaseModel instance.
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Generates a string representation of the object.

        Returns:
            str: String representation of the object.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute of an object and saves the object to storage.

        Example Usage:
        obj = BaseModel()
        obj.save()

        Inputs:
        - None

        Flow:
        1. The 'save' method is called on an instance of the 'BaseModel' class.
        2. The 'updated_at' attribute of the object is updated with the current datetime.
        3. The 'save' method of the 'storage' object is called to save the object to storage.

        Outputs:
        - None
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Converts the object to a dictionary representation.

        Returns:
            dict: Dictionary representation of the object.
        """
        class_dict = {
            "__class__": self.__class__.__name__
        }
        for k, v in self.__dict__.items():
            if k == "created_at":
                class_dict[k] = v.isoformat()
            elif k == "updated_at":
                class_dict[k] = v.isoformat()
            else:
                class_dict[k] = v
        return class_dict
