#!/usr/bin/python3
"""Test for Base"""


import unittest
import os
import sys

from models.base import Base

p = os.path.abspath('.')
sys.path.insert(1, p)


class Testbase(unittest.Testbase):
    """Test for Base"""

    def test_0(my_base):
        tmp = Base()
        my_base.assertTrue(isinstance(tmp, Base))

    def test_1(my_base):
        tmp1 = Base()
        my_base.assertEqual(tmp1.id, 1)
        tmp2 = Base()
        my_base.assertEqual(tmp1.id, 2)
        tmp3 = Base()
        my_base.assertEqual(tmp1.id, 3)

    def test_2(my_base):
        tmp1 = Base(174)
        my_base.assertEqual(tmp1.id, 174)
        tmp2 = Base(2)
        my_base.assertEqual(tmp1.id, 2)
