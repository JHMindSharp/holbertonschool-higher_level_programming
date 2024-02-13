#!/usr/bin/python3
"""Checks if an object is exactly an instance of a class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class."""
    return type(obj) is a_class
