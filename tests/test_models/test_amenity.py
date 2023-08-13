#!/usr/bin/env python3
"""This is the Amenity test module"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """This is the TestAmenity istance object"""
    def test_amenity_attrs(self):
        """tets cases"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
