#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    res = my_list[:]
    res.reverse()
    for i in res:
        print("{:d}".format(i))
