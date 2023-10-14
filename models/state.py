#!/usr/bin/python3
"""
module that defines the State class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    A class representing a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Method to initialize the State class instance

        Args:
            args - variable arguments
            kwargs - key word arguments
        """
        super().__init__(*args, **kwargs)