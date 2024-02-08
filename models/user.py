#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class.

    Attributes:
        email (str): user's email.
        password (str): user's password.
        first_name (str): the user's first name.
        last_name (str): user's second name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
