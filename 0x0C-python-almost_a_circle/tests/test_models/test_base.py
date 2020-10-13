#!/usr/bin/python3
"""
unittest class Base
"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """
    tests for id
    """
    def test_base(self):
        b6 = Base(12)
        self.assertEqual(b6.id, 12)

if __name__ == "__main__":
    unittest.main()
