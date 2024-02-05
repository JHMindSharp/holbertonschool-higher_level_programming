#!/usr/bin/python3
"""Define a square based on 3-square.py"""


class Square:
    """declare a square class  with attribut size"""
    def __init__(self, size=0):
        self.size = size
    """ declare a getter of attribut size"""
    @property
    def size(self):
        return self.__size
    """declare a setter of value size

    args:
    Value: the value of size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
    """declare a area"""

    def area(self):
        return self.__size * self.__size
