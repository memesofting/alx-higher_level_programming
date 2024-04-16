#!/usr/bin/python3
"""
Module writes an object to a text file,
using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Function writes an object to a text file
    using JSON representation
    Args:
        my_obj: python object
        filename: file to be written to
    Returns:
        number of characters written
    """

    my_str = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        number = f.write(my_str)
    return number
