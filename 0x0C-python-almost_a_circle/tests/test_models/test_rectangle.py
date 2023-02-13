#!/usr/bin/python3
"""
Unittest for Rectangle Class
# run with python -m unittest discover tests
# run with python -m unittest tests/test_models/test_rectangle.py
"""


import os
# import pep8
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models import rectangle
Rectangle = rectangle.Rectangle


class TestBase(unittest.TestCase):
    """Tests for models/rectangle.py"""

    """Test attributes"""
    def test_all_attr_given(self):
        """Test all attributes match what's given"""
        r1 = Rectangle(10, 20, 1, 2, 99)
        self.assertTrue(r1.width == 10)
        self.assertTrue(r1.height == 20)
        self.assertTrue(r1.x == 1)
        self.assertTrue(r1.y == 2)
        self.assertTrue(r1.id == 99)

    def test_default_attr(self):
        """Test default attributes are set when not given"""
        r2 = Rectangle(3, 4)
        self.assertTrue(r2.width == 3)
        self.assertTrue(r2.height == 4)
        self.assertTrue(r2.x == 0)
        self.assertTrue(r2.y == 0)
        self.assertTrue(r2.id is not None)

    def test_attr_validated(self):
        """Test attributes are validated before set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 1, 1, 1, 1)
            Rectangle([10, 3], 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {20, }, 1, 1, 1)
            Rectangle(1, {"d": 20}, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, None, 1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, (30, 20), 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -20, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 1, -99, 1)

    def test_private_attr_access(self):
        """Test private attributes are not accessible"""
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    """Test args given"""
    def test_invalid_args(self):
        """Test too many args given throws error"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)
        """Test too little args given throws error"""
        with self.assertRaises(TypeError):
            Rectangle(1)
            Rectangle()
            Rectangle(None)

    """Test class"""
    def test_class(self):
        """Test class created is indeed Rectangle"""
        self.assertEqual(type(Rectangle(1, 2)), Rectangle)

    """Test methods"""
    def test_area(self):
        """Test method: area"""
        self.assertEqual(Rectangle(3, 4).area(), 12)
        self.assertEqual(Rectangle(8, 7, 0, 0).area(), 56)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
