#!/usr/bin/python3
"""Takes 2 arguments tosolves challenges ..."""
from requests
from sys
import argv
import get


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    com = get(url).json()
    try:
        for i in range(10):
            print("{}: {}".format(
                com[i].get("sha"),
                com[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
