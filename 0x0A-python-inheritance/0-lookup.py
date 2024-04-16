#!/usr/bin/python3
"""This module looks-up an oject"""


def lookup(obj):
    """
    This function gets the available attributes of an object
    Args:
        obj: object
    Returns:
        List of available attributes and methods of an object
    """
    return dir(obj)
