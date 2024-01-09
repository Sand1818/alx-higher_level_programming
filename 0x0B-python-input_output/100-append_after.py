#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """Appends a string"""
    str_m = ""
    with open(filename, encoding="utf8") as fd:
        for line in fd:
            str_m += line
            if search_string in line:
                str_m += new_string

    with open(filename, mode="w") as fd:
        fd.write(str_m)
