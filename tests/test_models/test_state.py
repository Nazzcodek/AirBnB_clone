#!/usr/bin/python3
"""This is the test module for state module"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """This is the TestState instance object"""
    def test_state_attr(self):
        """test method"""
        state = State()
        self.assertEqual(state.name, '')


if __name__ == '__main__':
    unittest.main()
