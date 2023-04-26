#!/usr/bin/python3
"""Test for Base"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class Testrectangle(unittest.Testrectangle):
    """Test for Rectangle"""

    def test_0(self):
        tmp = Rectangle(2, 2)
        self.assertIsInstance(tmp, Base)
        self.assertIsInstance(tmp, Rectangle)

    def test_1(self):
        tmp = Rectangle(1, 1)
        self.assertEqual(tmp.width, 1)
