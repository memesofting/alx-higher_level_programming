#!/usr/bin/python3
"""Defines a rectangle"""


class BaseGeometry:
    """Base class for geometry operations

    Methods:
        area: raises an exception 'it is not implemented'
        integer_validator: validates value to be a
        positive integer
    """

    def area(self):
        """function defines an area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value to be a positive integer
        Args:
            name: (str) variable
            value: (int) variable
        """

        self.name = name
        self.value = value

        # if isinstance(self.value, (bool, list, tuple)):
        # raise TypeError(f"{name} must be an integer")
        # if not isinstance(self.value, int):
        if type(self.value) is not int:
            raise TypeError(f"{name} must be an integer")
        if self.value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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


class Square(Rectangle):
    """Class defines a square that inherits from
    Rectangle class
    """

    def __init__(self, size):
        """Function instantiates square
        and validates properties with integer_validator
        Args:
            size: size of rectangle
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    # def area(self):
    #    """returns the area of a square"""

    #    return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
