#!/usr/bin/python3
"""Defines Rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """setters initialise instance variables"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets Width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Calculates perimeter"""
        if self.height == 0 or self.width == 0:
            return 0

        return (self.height + self.width) * 2

    def __str__(self):
        """String"""
        rectangle = ""
        if self.height == 0 or self.width == 0:
            return rectangle

        for h in range(self.height - 1):
            rectangle += "#" * self.width + "\n"
        rectangle += "#" * self.width
        return rectangle
