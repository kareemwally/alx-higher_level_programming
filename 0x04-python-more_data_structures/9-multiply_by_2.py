#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = dict()
    for i, k in a_dictionary.items():
        res[i] = 2 * k
    return res
