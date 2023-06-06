#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i != 8:
            print("{0}{1}, ".format(i, j), end='')
        else:
            print("{0}{1}".format(i, j))
