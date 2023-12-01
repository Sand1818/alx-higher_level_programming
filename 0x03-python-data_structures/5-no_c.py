#!/usr/bin/python3
def no_c(my_string):
    n_string = [x for x in my_string if x != 'c' or x != 'C']
    return ("".join(n_string))
