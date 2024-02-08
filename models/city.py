#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """city class.

    Attributes:
        state_id (str): state's id.
        name (str): city name.
    """

    state_id = ""
    name = ""
