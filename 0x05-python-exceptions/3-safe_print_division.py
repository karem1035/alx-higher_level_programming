#!/usr/bin/python3
def safe_print_division(a, b):
    sun = 0
    try:
        sun = a / b
    except (TypeError, ValueError, ZeroDivisionError):
        sun = None
    finally:
        print("Inside result: {}".format(sun))
        return (sun)
