#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    res = my_list[:]
    if idx >= 0 and idx < len(my_list):
        res[idx] = element
    return res
