#!/usr/bin/python3
"""Function that returns a list of attributes and methods."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
