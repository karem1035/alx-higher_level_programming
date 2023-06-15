#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    for i in range(len(my_list)):
        new_list.append(my_list[i])
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
