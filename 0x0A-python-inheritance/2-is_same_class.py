#!/usr/bin/python3
"""Checks if an object is exactly an instance of the
specified class
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the
    specified class
    Returns:
        True if object is an instance
        False if object is not an instance
    """

    return type(obj) is a_class
