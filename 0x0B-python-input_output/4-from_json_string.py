#!/usr/bin/python3
"""a function that returns an object represented by a JSON string:"""

import json


def from_json_string(my_str):
    """returns an object represented by a JSON string

    Args:
        my_str (json str): must be converted to py obj

    Returns:
        a_dict (python obj): the converted str
    """
    a_dict = json.loads(my_str)
    return a_dictw
