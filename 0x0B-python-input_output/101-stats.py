#!/usr/bin/python3
import sys


def print_status():
    coun = 0
    siz = 0
    f_siz = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    for l in sys.stdin:
        line = l.split()
        try:
            siz += int(line[-1])
            code = line[-2]
            status_codes[code] += 1
        except:
            continue
        if coun == 9:
            print("File siz: {}".format(siz))
            for key, val in sorted(status_codes.items()):
                if (val != 0):
                    print("{}: {}".format(key, val))
            coun = 0
        coun += 1
    if coun < 9:
        print("File siz: {}".format(siz))
        for key, val in sorted(status_codes.items()):
            if (val != 0):
                print("{}: {}".format(key, val))


if __name__ == "__main__":
    print_status()
