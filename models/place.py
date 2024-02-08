#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """place class.

    Attributes:
        city_id (str): City's id.
        user_id (str): User's id.
        name (str): place's name.
        description (str): description of the place.
        number_rooms (int): number of rooms of the place.
        number_bathrooms (int): number of bathrooms in the place.
        max_guest (int): maximum number of guests in the place.
        price_by_night (int): price by night of the place.
        latitude (float): lat of the place.
        longitude (float): long of the place.
        amenity_ids (list): list in amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
