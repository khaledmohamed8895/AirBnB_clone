#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """state class.

    Attributes:
        name (str): the state's name.
    """

    name = ""
