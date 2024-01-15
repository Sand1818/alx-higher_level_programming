#!/usr/bin/python3
"""rectangle mmodel"""
from models.base import Base


class Rectangle(Base):
    """Claas Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initiliasation  .method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setting the width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """return height"""
        return(self.__height)

    @height.setter
    def height(self, height):
        """setting the height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """return x"""
        return(self.__x)

    @x.setter
    def x(self, x):
        """setting x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """returns y"""
        return(self.__y)

    @y.setter
    def y(self, y):
        """sets y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates the area of rectangle"""
        return self.width*self.height

    def display(self):
        """display function"""
        for l in range(self.y):
                print("")
        for i in range(self.height):
            for k in range(self.x):
                    print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """string method"""
        msg = '[Rectangle] ({}) {}/{} - {}/{}'
        return msg.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update methodology"""
        if args is not None and len(args) != 0:
            if len(args) >= 1 and len(args) != 0:
                self.id = args[0]
            if len(args) >= 2 and len(args) != 0:
                self.width = args[1]
            if len(args) >= 3 and len(args) != 0:
                self.height = args[2]
            if len(args) >= 4 and len(args) != 0:
                self.x = args[3]
            if len(args) >= 5 and len(args) != 0:
                self.y = args[4]
        else:
            for k, v in kwargs.items():
                if hasattr(self, k) is True:
                    setattr(self, k, v)

    def to_dictionary(self):
        """to_dictionary method"""
        a = {}
        a["x"] = self.x
        a["y"] = self.y
        a["id"] = self.id
        a["height"] = self.height
        a["width"] = self.width
        return a
