#!/usr/bin/python3
""" Module for Base Model """


import uuid
import datetime
class BaseModel:
    """
    Defines a base class with common attributes and methods for other classes.

    Attributes:
        id (str): A unique identifier for each object.
        created_at (datetime): The date and time when the object was created.
        updated_at (datetime): The date and time when the object was last updated.
    """

    def __init__(self) -> None:
        """
        Initializes the object by setting the id, created_at, and updated_at fields.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at field with the current date and time.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Converts the object to a dictionary representation.

        Returns:
            dict: A dictionary representation of the object.
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict
