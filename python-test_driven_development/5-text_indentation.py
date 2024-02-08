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

    special_chars = ['.', '?', ':']
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in special_chars:
            print("\n")
            if i < len(text) - 1 and text[i + 1] == ' ':
                i += 1
        i += 1
    print("", end="")
