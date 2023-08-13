#!/usr/bin/python3
"""
This is the user model that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """this is the user instance object"""
    email = "" 
    password = ""
    first_name = ""
    last_name = ""
