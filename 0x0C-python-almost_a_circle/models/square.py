#!/usr/bin/python3
"""Square class module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.validator("width", value)
        self.validator("height", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update assigns arguments to rectangle attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return string represntation of Rectangle object"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def to_dictionary(self):
        """Resturns a dictionary representation of Rectangle"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
