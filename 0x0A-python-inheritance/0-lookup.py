#!/usr/bin/python3
def lookup(obj):
    """A function that taks a Calss and returns its components

    Args:
        obj : The object we are going to use

    Returns:
        str : returns the list of available attributes and methods of an object
    """

    return (dir(obj))
