#!/usr/bin/python3
""" Script takes URL and enmail and sends POST displays body"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    info = urllib.parse.urlencode({"email": sys.argv[2]})
    info = info.encode('ascii')
    req = urllib.request.Request(sys.argv[1], info)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode())
