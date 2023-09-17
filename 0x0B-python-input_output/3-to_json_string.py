#!/usr/bin/python3
'''a function that returns the JSON representation of an object (string):'''

import json


def to_json_string(my_obj):
    """Dumps a dic to json strn

    Args:
        my_obj (dict): dumps it a json string

    Returns:
        a_string: the string result
    """
    a_string = json.dumps(my_obj)
    return a_string
