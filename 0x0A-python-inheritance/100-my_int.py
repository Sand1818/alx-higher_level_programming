#!/usr/bin/python3
"""
Class Intinger
"""


class MyInt(int):

    def __ne__(self, value):
        if isinstance(value, int):
            return value == value
        return False

    def __eq__(self, value):
        return not self.__ne__(value)
