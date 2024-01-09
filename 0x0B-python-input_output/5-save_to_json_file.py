#!/usr/bin/python3
""""JSON """
import json


def save_to_json_file(my_obj, filename=""):
    """Save an object to a JSON file."""
    with open(filename, mode="w") as fd:
        json.dump(my_obj, fd)
