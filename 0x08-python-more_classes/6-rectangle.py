#!/usr/bin/python3
"""
Class Rectagle
"""


class Rectangle:
    """Defines a Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantiation attributes"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Calculates area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates permiter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Prints the rectangle using #s"""
        sq = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    sq += "#"
                if i < self.__height - 1:
                    sq += "\n"
        return sq

    def __repr__(self):
        """Return the rectangle"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Print message when instance is  deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
