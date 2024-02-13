#!/usr/bin/python3
"""Expands Square class with improved __str__ method."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""
    def __init__(self, size):
        """Initialize Square with size."""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the square description."""
        return f"[Square] {self.__size}/{self.__size}"
