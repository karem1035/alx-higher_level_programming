#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file:
"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
    __import__("6-load_from_json_file").load_from_json_file

    args_list = []

    if len(sys.argv) > 1:
        args_list = list(sys.argv[1:])
        print(args_list)

    with open("add_item.json", "r", encoding="UTF8") as a_file:
        obj = load_from_json_file(a_file)
        args_list += obj
        save_to_json_file(obj, a_file)
