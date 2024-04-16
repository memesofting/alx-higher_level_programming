#!/usr/bin/python3
"""This module retuns an object represented by a JSON string"""


import json


def from_json_string(my_str):
    """
    Function returns a python object
    """
    return json.loads(my_str)
