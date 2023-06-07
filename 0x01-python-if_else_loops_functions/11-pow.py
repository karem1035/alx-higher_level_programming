#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    n = abs(b)
    r = 1
    for i in range(n):
        r = r * a
    if b < 0:
        r = 1 / r
    return r
