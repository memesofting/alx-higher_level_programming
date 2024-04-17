#!/usr/bin/python3
"""Checks if an object is an instance of the
specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of or
    a class that inherited from the specified class
    Returns:
        True if object is an instance
        False if object is not an instance
    """

    return isinstance(obj, a_class)
