#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    san = 0
    try:
        for item in range(0, x):
            print("{}".format(my_list[item]), end="")
            san += 1
    except IndexError:
        pass
    print()
    return san
