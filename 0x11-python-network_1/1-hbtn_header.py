#!/usr/bin/python3
"""Displays values of X-Request-Id variables found in header"""
import urllib.request
import sys


if __name__ == "__main__":
    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        content = response.info()["X-Request-Id"]
        print(content)
