#!/usr/bin/python3
""" Takes URL & email sends POST and displays bodyof response"""
import requests
import sys


if __name__ == "__main__":
    info = {"email": sys.argv[2]}
    respon = requests.post(sys.argv[1], data=info)
    print(respon.text)
