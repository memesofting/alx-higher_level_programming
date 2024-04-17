#!/usr/bin/python3
"""Defines a rectangle"""


import importlib
BaseGeometry = importlib.import_module('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class defines a rectangle inheriting properties
    from BaseGeometry class
    """

    def __init__(self, width, height):
        """Function instantiates rectangle
        and validates properties with integer_validator
        Args:
            width: width of rectangle
            height: height of rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
