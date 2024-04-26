#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request


if __name__ == '__main__':
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        fetched_content = response.read()
        print("Body response:")
        print(f"\t- type: {type(fetched_content)}")
        print(f"\t- content: {fetched_content}")
        print(f"\t- utf8 content: {fetched_content.decode()}")
