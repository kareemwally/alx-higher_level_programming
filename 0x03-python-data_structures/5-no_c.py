#!/usr/bin/python3
def no_c(my_string):
    m = my_string.split('C')
    n = "".join(m)
    res = n.split('c')
    return "".join(res)
