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
    if a is None or b is None:
        raise TypeError("add() missing 2 required positional arguments: 'a' and 'b'")
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
    doctest.testfile("tests/0-add_integer.txt")
