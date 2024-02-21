import unittest
from models.rectangle import Rectangle

class TestWidthHeight(unittest.TestCase):
    """Test cases for the width and height setter/getter."""

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

if __name__ == '__main__':
    unittest.main()
