#!/usr/bin/python3
"""Defines Amenity class that inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representation of Amenity"""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity"""
        super().__init__(*args, **kwargs)
        self.name = ""

