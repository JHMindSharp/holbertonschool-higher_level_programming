#!/usr/bin/python3
"""Defines a class BaseGeometry with public instance methods."""


class BaseGeometry:
    """A class with public instance methods."""

    def area(self):
        """Raises an Exception with a message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
