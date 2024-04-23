#!/usr/bin/python3
"""Tis is a base class module"""


class Base:
    """Tis is a base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is a class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
