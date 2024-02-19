#!/usr/bin/python3
"""Write an object to a file using JSON representation."""


import json


def save_to_json_file(my_obj, filename):
    """
    Write `my_obj` to `filename` using JSON.

    Args:
        my_obj (Any): The object to serialize.
        filename (str): The name of the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
