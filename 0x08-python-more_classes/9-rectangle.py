#!/usr/bin/python3
"""
    Defines a Rectangle
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialisingthe instance variables"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns the private variable"""
        return self.__width

    @width.setter
    def width(self, value):
        """
            Checking for TypeError and ValueErrorn and 
            then setting up the private var
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returning the private variable """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Checking for TypeError and ValueError and 
            then setting up the private var
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Calculates the perimeter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return 0

        return (self.height + self.width) * 2

    def __str__(self):
        """returns a string representation of the rectangle"""
        symbol = str(self.print_symbol)
        rectangle = ""
        if self.height == 0 or self.width == 0:
            return rectangle

        for h in range(self.height - 1):
            rectangle += symbol * self.width + "\n"
        rectangle += symbol * self.width
        return rectangle

    def __repr__(self):
        """recreation of instance call"""
        rep = "{}({}, {})".format(self.__class__.__name__,
                                  self.width, self.height)
        return rep

    def __del__(self):
        """prints message when rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Checks whether the rectangles are bigger or equal"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        elif rect_1.area() >= rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Creates a Rectangle with width and height are size"""
        return cls(size, size)
