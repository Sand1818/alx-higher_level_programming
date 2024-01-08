#!/usr/bin/python3
""""Function that adds attribute to an object if possible"""


def add_attribute(cls, name, first):
    if not hasattr(cls, name):
        raise TypeError("can't add new attribute")
    cls.name = first
