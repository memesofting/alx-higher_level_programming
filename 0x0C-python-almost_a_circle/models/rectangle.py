#!/usr/bin/python3
"""This is a base class module"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises rectangle class"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validator("y", value)
        self.__y = value

    def area(self):
        """Gets the area of rectangle
        Returns:
            area = width * height
        """
        a = self.width * self.height
        if self.width == 0 or self.height == 0:
            a = 0
            return a
        else:
            return a

    def display(self):
        """Method prints to standard output the Rectangle instance
        with character '#'
        """
        for i in range(self.height):
            for i in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """Return string represntation of Rectangle object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )
