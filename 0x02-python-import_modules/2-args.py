#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]

    n_args = len(argv)

    if n_args == 0:
        print("0 arguments" + (":" if n_args > 0 else "."))
    else:
        print("{} argument{}:".format(n_args, 's' if n_args != 1 else ''))

        rank = 1
        for arg in argv:
            print("{}: {}".format(rank, arg))
            rank += 1
