#!/usr/bin/python3
"""Adds a public instance method to BaseGeometry."""


class BaseGeometry:
    """Class BaseGeometry with public instance method."""
    def area(self):
        """Raise an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")
