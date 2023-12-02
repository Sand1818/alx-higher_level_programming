#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    san = []
    for i in my_list:
        if i % 2 == 0:
            san.append(True)
        else:
            san.append(False)
    return (san)
