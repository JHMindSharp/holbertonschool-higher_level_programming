#!/usr/bin/python3
"""Module initiate a Base class"""


class Base:
    """The Base class taking nb objects in private """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance.

        Args:
            id (int, optional): The identifier. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
