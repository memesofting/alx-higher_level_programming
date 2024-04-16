#!/usr/bin/python3
"""Tis module appends to the content of a file"""


def append_write(filename="", text=""):
    """
    This function appends a string of text to a txt file
    Args:
        filename: file to be written to
        text: string to be written to file
    Returns:
        filename with overwritten text
    """
    with open(filename, 'a', encoding="utf-8") as f:
        number = f.write(text)
    return number
