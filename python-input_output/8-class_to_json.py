#!/usr/bin/python3
"""Module to retrieve dictionary description for JSON serialization."""


def class_to_json(obj):
    """
    Return dictionary description for `obj` for JSON serialization.

    Args:
        obj (Any): The object to serialize.

    Returns:
        dict: Dictionary description of `obj`.
    """
    return obj.__dict__
