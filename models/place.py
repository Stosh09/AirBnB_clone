#!/usr/bin/python3
"""
module defining Place class
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    A class that represents a place.

    Attributes:
        city_id (str): The ID of the city.
        user_id (str): The ID of the user.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number
        of guests allowed in the place.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of amenity IDs for the place.
    """

    city_id = ""
    user_id = ""
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0

    def __init__(self, *args, **kwargs):
        """
        Initializes a Place object with the given arguments.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.

        Example Usage:
            place = Place(city_id="123", name="Cozy Apartment")
            In this example, a Place object is created
            with the city_id attribute set to "123" and
            the name attribute set to "Cozy Apartment".

        Returns:
            None. The __init__ method does not return anything.
        """
        super().__init__(*args, **kwargs)
