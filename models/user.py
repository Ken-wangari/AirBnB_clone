#!/usr/bin/python3
"""Defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new User.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")

    def to_dict(self):
        """Return the dictionary of the User instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = super().to_dict()
        rdict["email"] = self.email
        rdict["password"] = self.password
        rdict["first_name"] = self.first_name
        rdict["last_name"] = self.last_name
        return rdict

    def __str__(self):
        """Return the print/str representation of the User instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.to_dict())

