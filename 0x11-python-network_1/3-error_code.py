#!/usr/bin/python3
"""Takes in URL, sends request and displays the body """
import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode())
    except urllib.error.URLError as error:
        print(f"Error code: {error.code}")
