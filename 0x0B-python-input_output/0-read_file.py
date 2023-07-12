#!/usr/bin/python3
"""Function read a file"""


def read_file(filename=""):
    """This function that reads a text file (UTF8)
    and prints it to stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
