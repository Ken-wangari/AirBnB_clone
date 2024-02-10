#!/usr/bin/python3
"""Initialization of FileStorage for models directory"""
from models.engine.file_storage import FileStorage

def initialize_storage():
    """Initialize the FileStorage instance and reload data"""
    storage = FileStorage()
    storage.reload()

if __name__ == "__main__":
    initialize_storage()

