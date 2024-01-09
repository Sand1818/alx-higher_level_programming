#!/usr/bin/python3
"""Appends string at the end offile"""


def append_write(filename="", text=""):
    """A function that appends a string end of file"""

    with open(filename, mode="a", encoding="utf-8") as appendFile:
        return appendFile.write(text)
