#!/usr/bin/python3
"""Square class implementation"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns width"""
        return self.width

    @size.setter
    def size(self, val):
        """size setter (width & height)"""
        self.setter_validation("width", val)
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """Update function in the class """

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """str method overwrite"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """to dictionary represanting class"""
        return {'id': getattr(self, "id"),
                'x': getattr(self, "x"),
                'size': getattr(self, "size"),
                'y': getattr(self, "y")}
