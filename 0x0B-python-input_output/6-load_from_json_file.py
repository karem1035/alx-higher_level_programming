#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from JSON file"""
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
