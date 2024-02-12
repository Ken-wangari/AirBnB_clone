#!/usr/bin/python3
"""City module"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class"""

    def __init__(self, *args, **kwargs):
        """City constructor"""

        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""

    def __str__(self):
        """String representation of City"""

        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """Returns dictionary representation of City"""

        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = type(self).__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy

