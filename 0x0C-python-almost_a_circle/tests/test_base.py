#!/usr/bin/python3
"""Test for Base"""


import unittest
from models.base import Base

class Testbase(unittest.Testbase):
    """Test for Base"""

    def test_0(self):
        tmp = Base()
        self.assertTrue(isinstance(tmp, Base))

    def test_1(self):
        tmp1 = Base()
        self.assertEqual(tmp1.id, 1)
        tmp2 = Base()
        self.assertEqual(tmp1.id, 2)
        tmp3 = Base()
        self.assertEqual(tmp1.id, 3)

    def test_2(self):
        tmp1 = Base(174)
        self.assertEqual(tmp1.id, 174)
        tmp2 = Base(2)
        self.assertEqual(tmp1.id, 2)
