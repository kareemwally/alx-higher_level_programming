#!/usr/bin/python3
def add_tuple(tuple_a=(0, 0), tuple_b=(0, 0)):
    a = find_none(tuple_a)
    b = find_none(tuple_b)
    res = (a[0] + b[0], a[1] + b[1])
    return res


def find_none(a):
    res = list(a)
    i = 2 - len(res)
    for j in range(i):
        res.append(0)
    return(tuple(res))
