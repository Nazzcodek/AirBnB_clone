#!/usr/bin/python3

import unittest
import uuid

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """Tests the __init__ method."""
        model = BaseModel()
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

    def test_class_doc(self):
        """ Test BaseModel instance documentation"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_method_docs(self):
        """ Test BaseModel methods documentation"""
        methods = [
            BaseModel.__init__, BaseModel.__str__,
            BaseModel.save, BaseModel.to_dict
        ]
        for i in methods:
            self.assertIsNotNone(i.__doc__)

    def test_initial_attribute(self):
        """ Test object id"""
        test_model = BaseModel()
        test_model2 = BaseModel()

        # check if id exists, not NULL and a string
        self.assertTrue(hasattr(test_model, 'id'))
        self.assertIsNotNone(test_model.id)
        self.assertIsInstance(test_model.id, str)

        # Check if id is uuid
        self.assertTrue(uuid.UUID(test_model.id))

        # Check if two instances have the same id
        self.assertNotEqual(test_model.id, test_model2.id)

        # Check if created_at exist, not NULL, and it's from datetime
        self.assertTrue(hasattr(test_model, 'created_at'))
        self.assertIsNotNone(test_model.created_at)
        self.assertIsInstance(test_model.created_at, datetime)

        # Check if updated_at exist, not NULL, and it's from datetime
        self.assertTrue(hasattr(test_model, 'updated_at'))
        self.assertIsNotNone(test_model.updated_at)
        self.assertIsInstance(test_model.updated_at, datetime)

        # Check if updated_at time is after created_at
        self.assertGreater(test_model.updated_at, test_model.created_at)

        # Check that *args was not used
        test_with_arg = BaseModel("args")
        self.assertNotIn("args", test_with_arg.__dict__)

        # Check if __str__ prints correct output
        str_ = "[BaseModel] ({}) {}".format(test_model.id, test_model.__dict__)
        self.assertEqual(str(test_model), str_)


if __name__ == '__main__':
    unittest.main()
