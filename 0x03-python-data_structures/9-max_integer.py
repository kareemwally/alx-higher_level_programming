#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    res = my_list[0]
    for i in my_list:
        if i >= res:
            res = i
    return res
