import unittest
from models.rectangle import Rectangle

class TestInvalidInitialization(unittest.TestCase):
    """Test cases for invalid initialization of Rectangle."""

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

if __name__ == '__main__':
    unittest.main()
