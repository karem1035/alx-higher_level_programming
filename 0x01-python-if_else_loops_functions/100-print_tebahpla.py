#!/usr/bin/python3
for i in reversed(range(26)):
    letter = 0
    if i % 2 == 1:
        letter = letter + i + 97
    else:
        letter = letter + i + 65
    print("{}".format(chr(letter)), end='')
