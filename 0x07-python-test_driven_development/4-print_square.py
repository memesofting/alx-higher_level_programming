#!/usr/bin/python3
"""This module prints a square with the character #"""


def print_square(size):
    """
    This function prints a square
    Args:
        size: length of the square
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end='')
            print()
    pass


if __name__ == "__main__":
    import doctest
    doctest.testfile()
