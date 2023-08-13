#!/usr/bin/python3
"""
class user that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    USER CLASS that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
