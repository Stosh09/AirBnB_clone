#!/usr/bin/python3
"""
Module that defines class User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    A class representing a user.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Method to initialize the User class instance

        Args:
            args - variable arguments
            kwargs - key word arguments
        """
        super().__init__(*args, **kwargs)