#!/usr/bin/python3
def no_c(my_string):
    n_str = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            n_str += i
    return n_str
