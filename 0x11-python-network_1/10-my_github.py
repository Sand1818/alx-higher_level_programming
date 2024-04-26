#!/usr/bin/python3
""" Takes github credentials and display your id"""
import sys
import requests
import json


if __name__ == '__main__':
    headers = {'Accept': 'application/vnd.github+json',
               'Authorization':  f'Bearer {sys.argv[2]}',
               'X-GitHub-Api-Version': '2022-11-28'}
    res = requests.get('https://api.github.com/user', headers=headers,)
    try:
        respon = res.json()
        if (respon):
            print(f'{respon.get("id")}')
    except json.JSONDecodeError:
        print('None')
