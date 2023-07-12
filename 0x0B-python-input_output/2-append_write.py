#!/usr/bin/python3
"""Function that appends a string"""


def append_write(filename="", text=""):
    """Function that appends a string at the end
    of a text file (UTF8) and returns the number
    of characters added"""

    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)

    return len(text)
