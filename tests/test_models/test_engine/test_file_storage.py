#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Unittests for testing FileStorage class methods."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        self.storage._FileStorage__objects = {}
        self.storage._FileStorage__file_path = "file.json"

    def test_all(self):
        self.assertEqual(dict, type(self.storage.all()))

    def test_new(self):
        bm = BaseModel()
        self.assertIn("BaseModel." + bm.id, self.storage.all().keys())
        self.assertIn(bm, self.storage.all().values())

    def test_save(self):
        bm = BaseModel()
        self.storage.save()
        with open("file.json", "r") as f:
            save_dict = json.load(f)
        self.assertIn("BaseModel." + bm.id, save_dict.keys())

    def test_reload(self):
        bm = BaseModel()
        self.storage.save()
        self.storage.reload()
        objs = self.storage.all()
        self.assertIn("BaseModel." + bm.id, objs.keys())
        self.assertIsInstance(objs["BaseModel." + bm.id], BaseModel)

    def test_save_reload_multiple_classes(self):
        bm = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        self.storage.save()
        self.storage.reload()

        objs = self.storage.all()

        self.assertIn("BaseModel." + bm.id, objs.keys())
        self.assertIn("User." + user.id, objs.keys())
        self.assertIn("State." + state.id, objs.keys())
        self.assertIn("Place." + place.id, objs.keys())
        self.assertIn("City." + city.id, objs.keys())
        self.assertIn("Amenity." + amenity.id, objs.keys())
        self.assertIn("Review." + review.id, objs.keys())


if __name__ == "__main__":
    unittest.main()

