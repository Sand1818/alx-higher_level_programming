#!/usr/bin/python3
"""Prints pascal triangl"""


def pascal_triangle(n):
    if n is None:
        return None
    if n <= 0:
        return ([])
    san = []
    jel = 1
    for i in range(n):
        mini = []
        for j in range(i + 1):
            if j is 0:
                jel = 1
            else:
                jel = jel * (i - j + 1)//j
            mini.append(jel)
        san.append(mini)
    return (san)
