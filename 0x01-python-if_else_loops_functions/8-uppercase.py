#!/usr/bin/python3
def uppercase(str):
    for s in str:
        print("{}".format(chr(ord(s) - 32)
                          if (ord(s) >= ord("a") and
                              ord(s) <= ord("z")) else s), end="")
    print()
