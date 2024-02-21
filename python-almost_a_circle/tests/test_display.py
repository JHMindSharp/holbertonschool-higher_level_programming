import unittest
import io
import unittest.mock
from models.rectangle import Rectangle

class TestDisplay(unittest.TestCase):
    """Test cases for the display method."""

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
