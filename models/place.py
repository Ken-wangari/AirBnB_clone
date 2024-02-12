#!/usr/bin/python3
"""Place module"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place class"""

    def __init__(self, *args, **kwargs):
        """Place constructor"""

        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

    def __str__(self):
        """String representation of Place"""

        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """Returns dictionary representation of Place"""

        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = type(self).__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy

