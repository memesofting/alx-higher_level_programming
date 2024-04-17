#!/usr/bin/python3
"""Base geometry module"""


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

        if not isinstance(self.value, int):
            raise TypeError("value must be an integer")
        if self.value <= 0:
            raise ValueError("value must be greater than 0")


if __name__ == "__main__":
    import doctest
    doctest.testfile()
