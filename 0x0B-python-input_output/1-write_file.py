#!/usr/bin/python3
"""Function that write a string file"""


def write_file(filename="", text=""):
    """Function that writes a strring file"""

    with open(filename, mode='w', encoding='utf-8') as write_File:
        return write_File.write(text)
