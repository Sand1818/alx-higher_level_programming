#!/usr/bin/python3
def no_c(my_string):
    cat = ''
    for s in my_string:
        if s == 'c' or s == 'C':
            s = ''
        cat += s
    return (cat)
