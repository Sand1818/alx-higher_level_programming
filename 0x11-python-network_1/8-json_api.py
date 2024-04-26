#!/usr/bin/python3
"""Sends POST request to http://0.0.0.0:5000/search_user"""
import requests
import sys


if __name__ == '__main__':
    try:
        val = sys.argv[1]
    except:
        val = ""
    respon = requests.post('http://0.0.0.0:5000/search_user', data={'q': val})
    try:
        print("[{}] {}".format(respon.json()['id'], respon.json()['name']))
    except ValueError:
        print("Not a valid JSON")
    except:
        print("No result")
