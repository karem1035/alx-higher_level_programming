#!/usr/bin/python3
"""a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """ Creates an Object from a “JSON file”

    Args:
        filename (file): the json file name

    Returns:
        any obj type: the object the has been read
    """
    with open(filename, "r", encoding="UTF8") as a_file:
        data = json.load(a_file)
        return data
