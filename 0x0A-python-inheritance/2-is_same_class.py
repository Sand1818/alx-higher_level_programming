#!/usr/bin/python3
"""
Checks whether objects have same class
"""


def is_same_class(obj, a_class):
    """
    Check if obj is of type a_class and returns True or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
