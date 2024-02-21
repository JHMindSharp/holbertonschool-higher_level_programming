#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

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

    def test_width_height(self):
        """Test width and height setter/getter."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

        r.width = 20
        r.height = 5
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 5)

        with self.assertRaises(TypeError):
            r.width = "hello"
            r.height = "world"
        with self.assertRaises(ValueError):
            r.width = -10
            r.height = -5

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
            r.y = "world"
        with self.assertRaises(ValueError):
            r.x = -5
            r.y = -10

    def test_area(self):
        """Test the area calculation."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)


if __name__ == '__main__':
    unittest.main()
