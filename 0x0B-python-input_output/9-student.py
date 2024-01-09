#!/usr/bin/python3
"""Student Class with student definition"""


class Student:
    """Student data"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary"""

        return self.__dict__
