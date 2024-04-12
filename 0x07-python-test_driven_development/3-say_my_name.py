#!/usr/bin/python3
"""This moduleprints full name"""


def say_my_name(first_name, last_name=""):
    """
    This function print full name
    Args:
        first_name: first name
        last_name: last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile()
