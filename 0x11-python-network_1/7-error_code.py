#!/usr/bin/python3
"""Displays the body of response"""
import sys
import requests


if __name__ == '__main__':
    respon = requests.get(sys.argv[1])
    if (respon.status_code < 400):
        print(respon.text)
    else:
        print(f'Error code: {respon.status_code}')
