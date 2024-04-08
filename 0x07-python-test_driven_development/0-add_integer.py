#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two intwgers and returns an integer
    """
    try:
        a = int(a)
        b = int(b)
    except(TypeError):

    result = a + b
    return result
