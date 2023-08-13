#!/usr/bin/env python3
"""
Unittest for ```FileStorage```
"""
import unittest
import os
from models.engine.file_storage import FileStorage
import models.engine.file_storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class TestFileStorage(unittest.TestCase):
    """ Test the ``FileStorage`` class"""

    __file_path = "file.json"

    def setUp(self):
        """ Execute before every case"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        self.storage = FileStorage()

    def tearDown(self):
        """ Execute after every test case"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_module_doc(self):
        """ Test for the module's documentation"""
        self.assertIsNotNone(models.engine.file_storage.__doc__)

    def test_class_doc(self):
        """ Test for the class documentation"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_initial_attributes(self):
        """Test it is a dictionary"""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        """Test the all method"""
        all_obj = self.storage.all()
        self.assertIsInstance(all_obj, dict)
        self.assertIs(all_obj, self.storage._FileStorage__objects)

    def test_new(self):
        """Test the new method"""
        base_model = BaseModel()
        self.storage.new(base_model)
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_new_user(self):
        """Test the new method with user"""
        user_model = User()
        self.storage.new(user_model)
        key = "{}.{}".format(user_model.__class__.__name__, user_model.id)
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_reload(self):
        """Test the reload method"""
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()
        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn("BaseModel." + base_model.id, text)

        base_model.name = "Updated name"
        base_model.save()

        new_storage = FileStorage()
        new_storage.reload()
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(key, self.storage._FileStorage__objects)
        reloaded_ins = new_storage.all()[key]

    def test_multiple_instances(self):
        """Create multiple instances and save"""
        base = BaseModel()
        user = User()
        place = Place()
        state = State()
        city = City()
        amen = Amenity()
        review = Review()

        self.storage.new(base)
        self.storage.new(user)
        self.storage.new(place)
        self.storage.new(state)
        self.storage.new(city)
        self.storage.new(amen)
        self.storage.new(review)
        self.storage.save()

        self.storage._FileStorage__objects = {}
        self.storage.reload()

        self.assertEqual(
            self.storage.all()[f"{BaseModel.__name__}.{base.id}"].to_dict(),
            base.to_dict(),
        )
        self.assertEqual(
            self.storage.all()[f"{User.__name__}.{user.id}"].to_dict(),
            user.to_dict(),
        )
        self.assertEqual(
            self.storage.all()[f"{Place.__name__}.{place.id}"].to_dict(),
            place.to_dict(),
        )
        self.assertEqual(
            self.storage.all()[f"{State.__name__}.{state.id}"].to_dict(),
            state.to_dict(),
        )
        self.assertEqual(
            self.storage.all()[f"{City.__name__}.{city.id}"].to_dict(),
            city.to_dict(),
        )
        self.assertEqual(
            self.storage.all()[f"{Amenity.__name__}.{amen.id}"].to_dict(),
            amen.to_dict(),
        )
        self.assertEqual(
            self.storage.all()[f"{Review.__name__}.{review.id}"].to_dict(),
            review.to_dict(),
        )

    def test_reload_with_no_file(self):
        """Test reload when json file doesn't exist does not raise error"""
        try:
            self.storage.reload()
        except FileNotFoundError:
            self.fail("Error raised")


if __name__ == "__main__":
    unittest.main()
