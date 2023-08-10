#!/usr/bin/python3

import unittest
import uuid

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """Tests the __init__ method."""
        model = BaseModel()
        self.assertEqual(model.id, str(uuid.uuid4()))
        self.assertEqual(model.created_at, datetime.now())
        self.assertEqual(model.updated_at, model.created_at)

    def test_save(self):
        """Tests the save method."""
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.created_at, model.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method."""
        model = BaseModel()
        dict_repr = model.to_dict()
        self.assertEqual(dict_repr['__class__'], model.__class__.__name__)
        self.assertEqual(dict_repr['created_at'], model.created_at.isoformat())
        self.assertEqual(dict_repr['updated_at'], model.updated_at.isoformat())

    def test_str(self):
        """Tests the __str__ method."""
        model = BaseModel()
        class_name = model.__class__.__name__
        expected_str = f"[{class_name}] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

if __name__ == '__main__':
    unittest.main()
