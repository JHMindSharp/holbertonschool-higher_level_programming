import unittest
import io
import unittest.mock
from models.rectangle import Rectangle

class TestDisplayWithXY(unittest.TestCase):
    """Test cases for the display method with x and y offsets."""

    def test_display_with_xy(self):
        """Test the display method with x and y offsets."""
        r = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n" + (" " * 2 + "#" * 2 + "\n") * 3
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
