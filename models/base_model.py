#!/usr/bin/python3
"""Defines BaseModel class for other classes to inherit"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialization method for BaseModel instances"""

        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns string representation of BaseModel instance"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute and saves the instance"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""

        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

