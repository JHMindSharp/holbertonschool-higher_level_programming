#!/usr/bin/python3
"""
This module provides a simple function for adding two integers.
The function add_integer checks the types of the input arguments
and returns their sum if they are int or float.
"""


def add_integer(a, b=98):
    """
    Return the addition of a and b, error if a and b are not integers/floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result
