#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """Defines Rectangle"""

    @property
    def width(self):
        """Gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """constructor"""
        self.height = height
        self.width = width

    def area(self):
        """ Calculates area"""
        return self.__width*self.__height

    def perimeter(self):
    """Calculate the rectangle's perimeters"""
        if self.width == 0 or self.__height == 0:
            return 0
        return (self.__width*2) + (self.__height*2)
