#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set(my_list)
    i_sum = 0
    for i in unique_set:
        i_sum += i
    return i_sum
