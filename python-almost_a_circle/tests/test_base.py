#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_id_assignment(self):
        """
        Test id assignment in the Base class.
        """
        base1 = Base()
        base2 = Base()
        base3 = Base(12)
        base4 = Base()

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 12)
        self.assertEqual(base4.id, 3)


if __name__ == "__main__":
    unittest.main()
