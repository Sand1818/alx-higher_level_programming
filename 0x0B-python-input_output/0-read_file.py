#!/usr/bin/python3
"""Reads files on UTF-8"""


def read_file(filename=""):
    """Function that readss the file on UTF-8"""

    with open(filename, mode='r', encoding='utf-8') as read_File:
        print(read_File.read(), end="")
