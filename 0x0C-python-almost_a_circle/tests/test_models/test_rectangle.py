#!/usr/bin/python3
"""
unittest rectangle.py
"""
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """
    test class Rectangle
    """
    def setUp(self):
        """
        this is for testing
        """
        self.test = Rectangle(6, 6, 6, 6, 6)

    def test_id(self):
        """
        test id
        """
        self.assertEqual(self.test.id, 6)

    def test_width(self):
        """
        test width
        """
        self.assertEqual(self.test.width, 6)

    def test_height(self):
        """
        test height
        """
        self.assertEqual(self.test.height, 6)

    def test_x(self):
        """
        test x
        """
        self.assertEqual(self.test.x, 6)

    def test_y(self):
        """
        test y
        """
        self.assertEqual(self.test.y, 6)

if __name__ == "__main__":
    unittest.main()
