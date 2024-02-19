#!/usr/bin/python3
"""Module to return an object represented by a JSON string."""


import json


def from_json_string(my_str):
    """
    Return an object represented by `my_str`.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        Any: The object represented by `my_str`.
    """
    return json.loads(my_str)
