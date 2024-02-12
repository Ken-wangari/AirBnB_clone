#!/usr/bin/python3
"""Defines unittests for models/place.py."""

import os
import unittest
from datetime import datetime
from time import sleep
from models.place import Place
from models import storage

class TestPlace(unittest.TestCase):
    """Unittests for the Place class."""

    def setUp(self):
        """Set up testing environment."""
        self.test_place = Place()

    def tearDown(self):
        """Clean up testing environment."""
        del self.test_place

    def test_instance(self):
        """Test if instance is correctly created."""
        self.assertIsInstance(self.test_place, Place)

    def test_id_type(self):
        """Test if id is of type str."""
        self.assertIsInstance(self.test_place.id, str)

    def test_created_at_type(self):
        """Test if created_at is an instance of datetime."""
        self.assertIsInstance(self.test_place.created_at, datetime)

    def test_updated_at_type(self):
        """Test if updated_at is an instance of datetime."""
        self.assertIsInstance(self.test_place.updated_at, datetime)

    def test_save(self):
        """Test if save method updates updated_at."""
        old_updated_at = self.test_place.updated_at
        sleep(0.1)
        self.test_place.save()
        self.assertNotEqual(old_updated_at, self.test_place.updated_at)

    def test_to_dict(self):
        """Test if to_dict method returns the correct dictionary."""
        test_dict = self.test_place.to_dict()
        self.assertIsInstance(test_dict, dict)
        self.assertIn('id', test_dict)
        self.assertIn('__class__', test_dict)
        self.assertIn('created_at', test_dict)
        self.assertIn('updated_at', test_dict)

    def test_str(self):
        """Test the __str__ method."""
        test_str = str(self.test_place)
        self.assertIn("[Place]", test_str)
        self.assertIn(str(self.test_place.id), test_str)

    def test_save_to_file(self):
        """Test if save method saves the object to file storage."""
        storage.save()
        filename = 'file.json'
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.assertIn('Place.' + self.test_place.id, lines[-1])

if __name__ == '__main__':
    unittest.main()

