#!/usr/bin/python3
""" Takes URL sends request and displaces value variable"""
import requests
import sys


if __name__ == "__main__":
    try:
        respon = requests.get(sys.argv[1])
        print(respon.headers['X-Request-Id'])
    except:
        pass
