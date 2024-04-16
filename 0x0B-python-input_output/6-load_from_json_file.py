#!/usr/bin/python3
"""Module creates object from a JSON file"""


import json


def load_from_json_file(filename):
    """Function creates an Object from a JSON file"""

    with open(filename, encoding="utf-8") as f:
        json.load(f)
