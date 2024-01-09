#!/usr/bin/python3
"""Defines Student class"""


class Student:
    """Contains Student data """
    def __init__(self, first_name, last_name, age):
        """Initilise attribute"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionarry"""
        a_dict = {}
        if attrs is not None:
            for i in range(len(attrs)):
                if attrs[i] in self.__dict__:
                    a_dict[attrs[i]] = self.__dict__[attrs[i]]
            return a_dict
        return self.__dict__

    def reload_from_json(self, json):
        for i in json:
            setattr(self, i, json[i])
