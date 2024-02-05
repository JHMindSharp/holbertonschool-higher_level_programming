#!/usr/bin/python3
"""Module to define a square based on 3-square.py"""


class Square:
    """Declare a Square class of integer size"""
    def __init__(self, size=0):
        """initialisation of square class

        args:
        size: The size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
