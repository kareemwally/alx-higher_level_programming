#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    res = my_list
    if idx in range(0, len(my_list)):
        del(res[idx])
    return res
