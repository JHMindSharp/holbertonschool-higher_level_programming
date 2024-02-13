#!/usr/bin/python3
"""Checks if an object inherited from a specified class."""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
