#!/usr/bin/python3
class Square:
    sca = None

    def __init__(self, size=0):
        if type(size) is int:
            if size >= 0:
                self.sca = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
