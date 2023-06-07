#!/usr/bin/python3
def pow(a, b):
    n = 1
    if b >= 0:
        for i in range(b):
            n = n * a
    else:
        for i in range(-b):
            n = n / a
    return n
