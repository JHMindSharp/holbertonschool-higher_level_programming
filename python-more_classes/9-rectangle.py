#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0  # Class variable to count instances
    print_symbol = '#'  # Class variable for print symbol

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle's area."""
        return self.width * self.height

    def perimeter(self):
        """Returns the rectangle's perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a printable representation of the rectangle"
        "using the `print_symbol`."""
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.width for _ in range(self.height)])

    def __repr__(self):
        """Returns a string representation of the rectangle to"
        "recreate a new instance."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is"
        "deleted and decrements the instance counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size."""
        return cls(size, size)
