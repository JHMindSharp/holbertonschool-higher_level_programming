#!/usr/bin/python3
import json
"""Create an object from a "JSON file"."""


def load_from_json_file(filename):
    """
    Create object from a JSON file named `filename`.

    Args:
        filename (str): The name of the file.

    Returns:
        Any: The object created from JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
