#!/usr/bin/python3
"""
    Inherits  from a list
"""


class MyList(list):
    """Prints a sorted list"""
    def print_sorted(self):
        print(sorted(self))
