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
    
    def validator(self, name, value):
        """validates value to be a positive integer
        Args:
            name: (str) variable
            value: (int) variable
        """

        self.name = name
        self.value = value
        
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

class Rectangle(Base):
    """Rectangle class inheriting from Base class"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises rectangle class"""
        
        super().__init__(id)
        self.validator("width", width)
        self.validator("height", height)
        self.validator("x", x)
        self.validator("y", y)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
        @property
        def width(self):
            return self.__width
        
        @width.setter
        def width(self, value):
            if value <= 0:
                raise ValueError(f"{value} must be > 0")
            else:
                self.__width = value
            
        @property
        def height(self):
            return self.__height
        
        @height.setter
        def height(self, value):
            if value <= 0:
                raise ValueError(f"{value} must be > 0")
            else:
                self.__height = value
        
        @property
        def x(self):
            return self.__x
        
        @x.setter
        def x(self, value):
            if not isinstance(value, int):
                raise TypeError(f"{value} must be an integer")
            if value < 0:
                raise ValueError(f"{value} must be >= 0")
            else:
                self.__x = value
        
        @property
        def y(self):
            return self.__y
        
        @y.setter
        def y(self, value):
            if not isinstance(value, int):
                raise TypeError(f"{value} must be an integer")
            if value < 0:
                raise ValueError(f"{value} must be >= 0")
            else:
                self.__y = value
