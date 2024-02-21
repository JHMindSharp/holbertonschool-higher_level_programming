#!/usr/bin/python3
import unittest
import io
import unittest.mock
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
        with self.assertRaises(TypeError):
            r.height = "world"
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(ValueError):
            r.height = -5

    def test_invalid_initialization(self):
        """Test initialization with invalid values."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "0", 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 0)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "0")
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

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

    def test_area(self):
        """Test the area calculation."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display_with_xy(self):
        """Test the display method with x and y offsets."""
        r = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n" + (" " * 2 + "#" * 2 + "\n") * 3
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display(self):
        """Test display method."""
        r1 = Rectangle(4, 6)
        expected_output = "####\n" * 6
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        r2 = Rectangle(2, 2)
        expected_output = "##\n" * 2
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
