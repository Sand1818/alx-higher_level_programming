#!/usr/bin/python3
def read_file(filename=""):
    """Reads the contents of a given file"""


    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
