#!/usr/bin/python3
"""Test for Base"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class Testrectangle(unittest.Testrectangle):
    """Test for Rectangle"""

    def test_0(my_rectangle):
        tmp = Rectangle(2, 2)
        my_rectangle.assertIsInstance(tmp, Base)
        my_rectangle.assertIsInstance(tmp, Rectangle)

    def test_1(my_rectangle):
        tmp = Rectangle(1, 1)
        my_rectangle.assertEqual(tmp.width, 1)


if __name__ == "__main__":
    unittest.main()
