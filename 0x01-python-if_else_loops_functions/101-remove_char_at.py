#!/bin/usr/python3
def remove_char_at(string, n):
    n_string = ""
    for i in range(len(string)):
        if i != n:
            n_string += string[i]
    return n_string
