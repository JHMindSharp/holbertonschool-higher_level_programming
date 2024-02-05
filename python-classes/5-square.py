#!/usr/bin/python3
"""Define a square  on base of 4-square.py"""


class Square:
    """declare a square class with attribut value

    Args:
    Value: the value of size"""
    def __init__(self, value=0):
        self.size = value

    """ declare the getter of size value"""
    @property
    def size(self):
        return self.__size

    """declare the setter of size value"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError(" size must be >= 0")
        self.__size = value

    """declare the area for value size*size"""
    def area(self):
        return self.__size * self.__size

    """declare the function my_print for printing square of value size"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
