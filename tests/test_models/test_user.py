#!/usr/bin/python3
"""This is the user test module"""
import unittest
from models.user import User


class UserTest(unittest.TestCase):
    """This is the instance for UserTest"""

    def test_user_ttrs(self):
        """test case"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.password, "")


if __name__ == '__main__':
    unittest.main()
