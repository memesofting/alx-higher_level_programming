#!/usr/bin/python3
"""This module defines a rectangle
calculate area and perimeter
"""


class Rectangle:
    """This class define a rectangle with
    height and width properties
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        a = self.__width * self.__height
        if self.__width == 0 or self.__height == 0:
            a = 0
            return a
        else:
            return a

    def perimeter(self):
        p = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            p = 0
            return p
        else:
            return p

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for i in range(self.__height):
            rect_str += "#" * self.__width
            if i < self.__height - 1:
                rect_str += "\n"
        return rect_str
