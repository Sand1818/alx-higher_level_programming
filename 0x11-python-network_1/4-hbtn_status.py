#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == '__main__':
    respon = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(respon.text))
    print("\t- content:", respon.text)
