#!/usr/bin/python3
"""inherits functions"""


def inherits_from(obj, a_class):
    """Checks whether obj inherits from a_class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
