#!/usr/bin/python3
"""A function that appends to a txt file"""


def append_write(filename="", text=""):
    """appending to text file

    Args:
        filename: the file name
        text: the text to be appended

    Return:
        the number of text to be added.
    """
    with open(filename, "a", encoding="UTF") as a_file:
        return a_file.write(text)
