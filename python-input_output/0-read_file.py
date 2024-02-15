#!/usr/bin/python3
"""
This module defines the read_file function. It reads the content of a text file
and prints it to stdout, ensuring proper file closure after reading.
"""


def read_file(filename=""):
    """
    Reads and prints the content of a text file to stdout.

    Opens the specified file in read-only mode and prints its content.
    Uses a context manager to ensure automatic file closure.

    Parameters:
    - filename (str): Path to the file. Defaults to an empty string, which
      will result in an error since no file name is specified.

    Returns:
    - None
    """
    with open(filename, "r") as file:
        print(file.read(), end="")


if __name__ == "__main__":
    read_file("my_file_0.txt")
