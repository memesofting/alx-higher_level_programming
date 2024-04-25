#!/usr/bin/python3
"""Square class module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string represntation of Rectangle object"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
