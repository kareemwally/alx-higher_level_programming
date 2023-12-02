#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    res = my_list[:]
    res.reverse()
    for i in res:
        print("{:d}".format(i))
