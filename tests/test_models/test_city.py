#!/usr/bin/python3
"""This is the test city module to for city module"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """This is the TestCity instance object"""
    def test_city_attrs(self):
        """This is the test method"""
        city = City()
        self.assertEqual(city.state_id, '')
        self.assertEqual(city.name, '')


if __name__ == '__main__':
    unittest.main()
