#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    san = 0
    jel = 0
    for item in my_list:
        san = san + (item[0] * item[1])
        jel = jel + item[-1]
    return (san/jel)
