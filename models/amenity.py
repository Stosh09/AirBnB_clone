#!/usr/bin/python3
"""
module defining Amenity class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A class representing an Amenity.

    Attributes:
        name (str): The name of the Amenity.

    Methods:
        __init__(*args, **kwargs): Initializes a new
        instance of the Amenity class.

    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the Amenity class.

        Args:
            self: The instance of the class itself.
            *args: Variable length argument list.
            **kwargs: Variable length keyword argument dictionary.

        Returns:
            None

        Summary:
        The __init__ method is a constructor method
        for the Amenity class. It is called when a
        new object of the Amenity class is created.

        Example Usage:
        amenity = Amenity()
        In this example, the __init__ method is called
        to initialize a new instance of the Amenity class.

        Code Analysis:
        Inputs:
        - self: The first parameter of the method,
        which refers to the instance of the class itself.
        - *args: Variable length argument list,
        which allows the method to accept any number of positional arguments.
        - **kwargs: Variable length keyword argument
        dictionary, which allows the method to accept any number of keyword arguments.

        Flow:
        1. The super() function is called with the __init__
        ethod of the parent class BaseModel as an argument.
        This initializes the attributes and methods inherited from the BaseModel class.
        2. The *args and **kwargs arguments are passed to
        the __init__ method of the parent class, allowing
        the Amenity class to accept and handle any additional
        arguments passed during object creation.

        Outputs:
        None. The __init__ method does not return any value. Its purpose is to initialize the object with the provided arguments and set its initial state.
        """
        super().__init__(*args, **kwargs)
