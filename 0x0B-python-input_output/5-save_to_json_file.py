#!/usr/bin/python3
"""Writes an Object to a text file, using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file

    Args:
        my_obj (python obj): a python object to be dumped
        filename (file): a file to write to it
    """
    with open(filename, "w") as a_file:
        json.dump(my_obj, a_file)
