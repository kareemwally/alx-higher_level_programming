#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    res = ""
    test = 0
    for i, k in a_dictionary.items():
        if k >= test:
            test = k
            res = i
    return res
