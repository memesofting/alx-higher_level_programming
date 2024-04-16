#!/usr/bin/python3
"""THis module reads a text file"""


def read_file(filename=""):
    """
    This function opens and reads a text file
    Args:
        filename: file to be read
    Returns:
        string from file
    """

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
