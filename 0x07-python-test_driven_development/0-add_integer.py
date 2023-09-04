#!/usr/bin/python3
"""

"""
def add_integer(a, b):
    if type(a) != int:
        raise TypeError("a must be float")
    if type(b) != int:
        raise TypeError("b must be float")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b