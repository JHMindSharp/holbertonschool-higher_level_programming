#!/usr/bin/python3
"""Module to define a square based on 1-square.py"""


class Square:
    """declare a square of attribut integer size"""
    def __init__(self, size=0):
        """initialisation of square class with attribut 'size'

        Args:
        size: The size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
