#!/usr/bin/python3
"""
module defining Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review for a place written by a user.

    Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the Review class.

        Args:
            *args: Variable length argument list.
            **kwargs: Variable length keyword argument list.

        Example Usage:
            review = Review(place_id="123", user_id="456", text="Great place!")

        Code Analysis:
            The __init__ method is called when a
            new instance of the Review class is created.
            It takes in any number of positional arguments (*args)
            and keyword arguments (**kwargs).
            The super().__init__(*args, **kwargs) line
            calls the constructor of the parent class (BaseModel)
            and passes the arguments to it.
            This initializes the attributes of
            the Review object with the provided values.

        Returns:
            None. The __init__ method does not return anything.
        """
        super().__init__(*args, **kwargs)
