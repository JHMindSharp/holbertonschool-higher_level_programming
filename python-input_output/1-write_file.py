#!/usr/bin/python3
"""Module for file writing.

This module provides a function for writing strings to text files,
overwriting if the file exists.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file.

    This function opens or creates a text file, writes the specified
    string, and closes the file. If the file exists, it overwrites it.

    Args:
        filename (str): The file path. Defaults to an empty file.
        text (str): The text to write. Defaults to empty.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w") as file:
        file.write(text)
    return len(text)
