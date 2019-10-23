#!/usr/bin/python3
""" Tests for class square """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ tests for class square """
    def test_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
