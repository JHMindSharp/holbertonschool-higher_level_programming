#!/usr/bin/python3
"""Module initiate a Base class"""
import json
import os
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the representation JSON of a dictionnary list."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writte the JSON representation of list_objs in a file."""
        filename = cls.__name__ + ".json"  # Nom du fichier basé sur la classe
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return a list of obj JSON representated by json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            list_dicts = cls.from_json_string(f.read())
            return [cls.create(**d) for d in list_dicts]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """_summary_

        Args:
            list_rectangles (_type_): _description_
            list_squares (_type_): _description_
        """
        turtle.speed(1)

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.color("red")
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)

        for sqr in list_squares:
            turtle.penup()
            turtle.goto(sqr.x, sqr.y)
            turtle.pendown()
            turtle.color("blue")
            for _ in range(4):
                turtle.forward(sqr.size)
                turtle.left(90)

        turtle.done()
