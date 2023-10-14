#!/usr/bin/python3
"""
module that defines the City class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    A class representing a city.

    Attributes:
    - state_id (str): The ID of the state the city belongs to.
    - name (str): The name of the city.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Method to initialize the City class instance

        Args:
            args - variable arguments
            kwargs - key word arguments
        """
        super().__init__(*args, **kwargs)
