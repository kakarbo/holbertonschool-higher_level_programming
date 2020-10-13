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

    def test_get_set_width(self):
        """
        test width getter/setter
        """
        self.test.width = 9
        self.assertEqual(self.test.width, 9)

    def test_height(self):
        """
        test height
        """
        self.assertEqual(self.test.height, 6)

    def test_get_set_height(self):
        """
        test height getter/setter
        """
        self.test.height = 9
        self.assertEqual(self.test.height, 9)

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

    def testNoArgs(self):
        """
        test no args
        """
        with self.assertRaises(TypeError):
            empty = Rectangle()

    def testUpdateArgs(self):
        """
        test update *args
        """ 
        self.test.update(8,8,8,8,8)
        self.assertEqual(self.test.id, 8)
        self.assertEqual(self.test.width, 8)
        self.assertEqual(self.test.height, 8)
        self.assertEqual(self.test.x, 8)
        self.assertEqual(self.test.y, 8)

    def testUpdateKwargsId(self):
        """
        test update **kwargs id
        """
        self.test.update(id=6)
        self.assertEqual(self.test.id, 6)

    def testUpdateKwargsWidht(self):
        """
        test update **kwargs width
        """
        self.test.update(width=6)
        self.assertEqual(self.test.width, 6)

    def testUpdateKwargsHeight(self):
        """
        test update **kwargs height
        """
        self.test.update(height=6)
        self.assertEqual(self.test.height, 6)

    def testUpdateKwargs_x(self):
        """
        test update **kwargs x
        """
        self.test.update(x=6)
        self.assertEqual(self.test.x, 6)

    def testUpdateKwargs_y(self):
        """
        test update **kwargs y
        """
        self.test.update(y=6)
        self.assertEqual(self.test.y, 6)

if __name__ == "__main__":
    unittest.main()
