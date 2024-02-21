import unittest
from models.rectangle import Rectangle

class TestArea(unittest.TestCase):
    """Test cases for the area calculation."""

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
