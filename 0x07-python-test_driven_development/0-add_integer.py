#!/usr/bin/python3
"""This module adds two integers"""


def add_integer(a, b=98):
    """
    Adds two intwgers and returns an integer
    Args:
        a: first integer
        b: second integer
    Returns:
        The sum of two integers
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    result = a + b
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
