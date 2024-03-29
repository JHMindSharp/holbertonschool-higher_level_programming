#!/usr/bin/python3
"""
This module provides a Rectangle class that inherits from Base.
"""

from .base import Base


class Rectangle(Base):
    """
    Represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle.
                Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle.
                Defaults to 0.
            id (int, optional): The id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle, must be an integer
                greater than 0.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle, must be an integer
                greater than 0.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Gets the x-coordinate of the rectangle.

        Returns:
            int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the rectangle.

        Args:
            value (int): The x-coordinate of the rectangle, must be a
            non-negative integer.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Gets the y-coordinate of the rectangle.

        Returns:
            int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the rectangle.

        Args:
            value (int): The y-coordinate of the rectangle, must be a
            non-negative integer.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Get the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__height * self.width

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        print("\n" * self.__y, end="")
        for row in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return the string representation of the Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args):
        """Assigns argument to each attribute.

        Args:
            *args: The arguments to be assigned to each attribute.
                1st argument: id attribute
                2nd argument: width attribute
                3rd argument: height attribute
                4th argument: x attribute
                5th argument: y attribute
                """
        attributes = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)

    def update(self, *args, **kwargs):
        """
        Updates the Rectangle instance attributes.

        Args:
            *args (tuple): Variable length argument list.
            **kwargs (dict): Arbitrary keyword arguments.
                key/value pairs representing attributes to update.

        Returns:
            None
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
