#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import io
from unittest.mock import patch
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Define unit test cases for the Rectangle class."""

    def test_width_height_initialization(self):
        """Test correct initialization of width and height."""
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)

    def test_x_y_initialization(self):
        """Test correct initialization of x and y."""
        r = Rectangle(10, 5, 3, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 2)

    def test_id_initialization(self):
        """Test correct initialization of id."""
        r = Rectangle(10, 5, 3, 2, 99)
        self.assertEqual(r.id, 99)

    def test_width_validation(self):
        """Test validation of width."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_height_validation(self):
        """Test validation of height."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_x_validation(self):
        """Test validation of x."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "0", 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 0)

    def test_y_validation(self):
        """Test validation of y."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "0")
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

    def test_area(self):
        """Test the area calculation."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        """Test the display method."""
        r = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)


    def test_str(self):
        """Test the __str__ method."""
        r = Rectangle(4, 6, 2, 1, 50)
        self.assertEqual(str(r), "[Rectangle] (50) 2/1 - 4/6")

    def test_update(self):
        """Test the update method."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")


if __name__ == "__main__":
    unittest.main()
