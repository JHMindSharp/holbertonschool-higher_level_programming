#!/usr/bin/python3
"""Defines Square class inheriting from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle."""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
