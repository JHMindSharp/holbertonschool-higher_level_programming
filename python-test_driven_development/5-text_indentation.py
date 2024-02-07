#!/usr/bin/python3
"""
This module defines a function text_indentation that prints
text with 2 new lines after each of these characters: ., ? and :.
"""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')
    print(new_text.strip())
