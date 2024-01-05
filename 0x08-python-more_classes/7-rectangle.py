#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """Defines a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    @property
    def width(self):
        """Retrieve rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the Rectangl's width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the Rectangl's height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """Rectangle's constructor"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def area(self):
        """Calculate the rectangle's area """
        return self.__width*self.__height

    def perimeter(self):
        """Calculate the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width*2) + (self.__height*2)

    def __str__(self):
        """
        Prints a rectangles
        """
        h = self.__height
        w = self.__width
        if h == 0 or w == 0:
            return ""
        mat = ""
        symbol = str(self.print_symbol)
        for j in range(h):
            mat = mat + symbol * w
            if j != h - 1:
                mat = mat + "\n"
        return mat

    def __repr__(self):
        """return a string representation of rectangle """
        return 'Rectangle({}, {})'.format(self.__width, self.height)

    def __del__(self):
        """prints Bye rectangle after rectangle is delected """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
