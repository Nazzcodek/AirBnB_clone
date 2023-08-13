#!/usr/bin/python3
"""This is the Review module that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is the review instance object"""
    place_id = ""
    user_id = ""
    text = "" 
