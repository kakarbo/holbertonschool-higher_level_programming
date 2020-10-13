#!/usr/bin/python3
"""
unittest square.py
"""
from models.square import Square
from models.rectangle import Rectangle
import unittest

class TestSquare(unittest.TestCase):
    """
    test class Square
    """

    def setUp(self):
        """
        this is for testing
        """
        self.test = Square(6, 6, 6, 6)

    def test_id(self):
        """
        test id
        """
        self.assertEqual(self.test.id, 6)

    def test_size(self):
        """
        test width
        """
        self.assertEqual(self.test.size, 6)

    def test_get_set_size(self):
        """
        test width getter/setter
        """
        self.test.size = 6
        self.assertEqual(self.test.width, 6)

    def test_x(self):
        """
        test x
        """
        self.assertEqual(self.test.x, 6)

    def test_get_set_x(self):
        """
        test x getter/setter
        """
        self.test.x = 9
        self.assertEqual(self.test.x, 9)

    def test_y(self):
        """
        test y
        """
        self.assertEqual(self.test.y, 6)

    def test_get_set_y(self):
        """
        test y getter/setter
        """
        self.test.y = 9
        self.assertEqual(self.test.y, 9)

    def testArea(self):
        """
        test area
        """
        self.assertEqual(self.test.area(), 36)

    def testDisplay(self):
        """
        test display
        """
        self.assertIsNone(self.test.display())

if __name__ == "__main__":
    unittest.main()
