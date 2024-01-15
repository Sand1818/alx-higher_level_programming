#!/usr/bin/python3
"""Testt for Base class"""

import unittest
from models.base import Base

class test_base__(unittest.TestCase):
    """ test base function"""
    def test(self):
        """tests"""
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        b = Base()
        self.assertEqual(b.id, 3)
        b = Base(15)
        self.assertEqual(b.id, 15)
        b = Base()
        self.assertEqual(b.id, 4)
        b = Base(2)
        self.assertEqual(b.id, 2)
        b = Base(-3)
        self.assertEqual(b.id, -3)
