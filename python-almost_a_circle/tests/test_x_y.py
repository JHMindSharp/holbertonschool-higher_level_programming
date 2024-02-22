#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestXY(unittest.TestCase):
    """Test cases for the x and y setter/getter."""

    def test_x_y(self):
        """Test x and y setter/getter."""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r.x = 5
        r.y = 10
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)

        with self.assertRaises(TypeError):
            r.x = "hello"
        with self.assertRaises(TypeError):
            r.y = "world"
        with self.assertRaises(ValueError):
            r.x = -5
        with self.assertRaises(ValueError):
            r.y = -10

if __name__ == '__main__':
    unittest.main()
