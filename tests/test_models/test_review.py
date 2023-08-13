#!/usr/bin/python3
"""This is the review test module"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """This is the TestReview instance object"""
    def test_review_attrs(self):
        """Test cases"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
