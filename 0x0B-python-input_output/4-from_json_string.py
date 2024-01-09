#!/usr/bin/python3
"""JSON object"""
import json


def from_json_string(my_str):
    """Return a python object represented by JSON"""

    return json.loads(my_str)
