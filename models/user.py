#!/usr/bin/python3
"""User module"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class"""

    def __init__(self, *args, **kwargs):
        """User constructor"""

        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        """String representation of User"""

        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """Returns dictionary representation of User"""

        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = type(self).__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy

