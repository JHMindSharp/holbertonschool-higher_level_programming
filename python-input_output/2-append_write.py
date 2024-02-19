#!/usr/bin/python3
"""Append a string at the end of a text file."""


def append_write(filename="", text=""):
    """
    Append `text` to a file named `filename`.

    Args:
        filename (str): The name of the file.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
