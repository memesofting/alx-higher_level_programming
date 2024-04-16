#!/usr/bin/python3
"""This module returns the JSON representation of a string"""


import json


def to_json_string(my_obj):
    """
    Function returns the json representation of an object
    """
    obj_str = json.dumps(my_obj)
    return obj_str
