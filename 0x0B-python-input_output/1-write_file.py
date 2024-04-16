#!/usr/bin/python3
"""Tis module overites the content of a file"""


def write_file(filename="", text=""):
    """
    This function writes a string of text to a txt file
    Args:
        filename: file to be written to
        text: string to be written to file
    Returns:
        filename with overwritten text
    """
    with open(filename, 'w', encoding="utf-8") as f:
        number = f.write(text)
    return number
