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

        # if isinstance(self.value, (bool, list, tuple)):
        #    raise TypeError(f"{name} must be an integer")
        #if not isinstance(self.value, int):
        if type(self.value) is not int:
            raise TypeError(f"{name} must be an integer")
        if self.value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    import doctest
    doctest.testfile()
