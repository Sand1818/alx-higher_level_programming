#!/usr/bin/python3
for s in range(0, 10):
    for j in range(s + 1, 10):
        if s == 8 and j == 9:
            print("{:d}{:d}".format(s, j))
        else:
            print("{:d}{:d}, ".format(s, j), end="")
