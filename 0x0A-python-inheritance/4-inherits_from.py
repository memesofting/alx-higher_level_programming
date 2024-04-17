#!/usr/bin/python3
"""Checks if an object is an instance of a class
that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class
    that inherited from the specified class
    Returns:
        True if object is an instance
        False if object is not an instance
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
