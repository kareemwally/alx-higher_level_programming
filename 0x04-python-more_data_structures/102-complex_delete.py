#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = dict()
    for i, k in a_dictionary.items():
        if k != value:
            new[i] = k
    a_dictionary = new
    return a_dictionary
