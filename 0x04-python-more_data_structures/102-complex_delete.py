#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    test = []
    for i, k in a_dictionary.items():
        if k == value:
            test.append(i)
    for c in test:
        del a_dictionary[c]
    return a_dictionary
