#!/usr/bin/python3
"""Function the writes to a file"""


def write_file(filename="", text=""):
    """write_tfile: writes to a file

    Args:
        filename (str, optional): the file to be read.
        text (str, optional): the text to be written.

    Returns:
        int : the numer of characters written
    """
    with open(filename, "w", encoding="UTF8") as a_file:
        return a_file.write(text)
