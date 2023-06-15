#!/usr/bin/python3
sum_argv = 0
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            sum_argv = sum_argv + int(sys.argv[i])
print(sum_argv)
