#!/usr/bin/python3
"""read_file function:
        reads file from the function argument
        and then prints it line by line.
"""


def read_file(filename=""):
    with open(filename, encoding="UTF8") as a_file:
        for a_line in a_file:
            print(a_line, end="")
