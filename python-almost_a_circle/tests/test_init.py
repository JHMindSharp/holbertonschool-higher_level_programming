#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestInit(unittest.TestCase):
    """Test cases for the initialization of Rectangle."""

    def test_init(self):
        """Test initialization of Rectangle."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10, 1, 1, 12)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 1)
        self.assertEqual(r2.id, 12)

if __name__ == '__main__':
    unittest.main()
