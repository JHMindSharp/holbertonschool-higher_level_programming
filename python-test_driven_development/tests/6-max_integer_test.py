#!/usr/bin/python3
"""
Unittest for max_integer function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the max_integer function."""

    def test_max_end(self):
        """Test with max at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_middle(self):
        """Test with max in the middle."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_element(self):
        """Test with only one element."""
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test with all negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)


if __name__ == '__main__':
    unittest.main()
