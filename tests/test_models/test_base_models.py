#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import os
import models


class TestBaseModel(unittest.TestCase):
    """Unittests for BaseModel class."""

    @classmethod
    def setUpClass(cls):
        """Set up for test."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Tear down for test."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_instantiation(self):
        """Test instantiation."""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))

    def test_unique_ids(self):
        """Test unique ids."""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_updated_at(self):
        """Test created_at and updated_at."""
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)
        self.assertEqual(bm.created_at, bm.updated_at)

    def test_save(self):
        """Test save method."""
        bm = BaseModel()
        first_updated_at = bm.updated_at
        sleep(0.1)
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_to_dict(self):
        """Test to_dict method."""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertIsInstance(bm_dict["created_at"], str)
        self.assertIsInstance(bm_dict["updated_at"], str)
        self.assertEqual(bm_dict["created_at"], bm.created_at.isoformat())
        self.assertEqual(bm_dict["updated_at"], bm.updated_at.isoformat())
        self.assertIn("id", bm_dict)

    def test_to_dict_kwargs(self):
        """Test to_dict method with kwargs."""
        dt = datetime.now()
        bm = BaseModel(id="123", created_at=dt, updated_at=dt)
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict["id"], "123")
        self.assertEqual(bm_dict["created_at"], dt.isoformat())
        self.assertEqual(bm_dict["updated_at"], dt.isoformat())

    def test_save_file(self):
        """Test save method updates file."""
        bm = BaseModel()
        bm.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as file:
            self.assertIn(bm.id, file.read())


if __name__ == "__main__":
    unittest.main()

