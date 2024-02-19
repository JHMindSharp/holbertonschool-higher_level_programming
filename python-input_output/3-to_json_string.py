#!/usr/bin/python3
import json
"""Module to return the JSON representation of an object."""


def to_json_string(my_obj):
    """
    Return the JSON representation of `my_obj`.

    Args:
        my_obj (Any): The object to serialize.

    Returns:
        str: JSON representation of `my_obj`.
    """
    return json.dumps(my_obj)
