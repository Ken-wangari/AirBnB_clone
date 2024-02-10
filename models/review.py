#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new Review.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.text = kwargs.get('text', "")

    def to_dict(self):
        """Return the dictionary of the Review instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = super().to_dict()
        rdict["place_id"] = self.place_id
        rdict["user_id"] = self.user_id
        rdict["text"] = self.text
        return rdict

    def __str__(self):
        """Return the print/str representation of the Review instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.to_dict())

