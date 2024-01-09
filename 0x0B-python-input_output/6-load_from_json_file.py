#!/usr/bin/python3
""""JSON file"""
import json


def load_from_json_file(filename):
    """Returns a created object fromJSON file"""

    with open(filename, mode="r", encoding="UTF-8") as readFile:
        return json.load(readFile)
