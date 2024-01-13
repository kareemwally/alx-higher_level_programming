#!/usr/bin/python3
"""
that function only add two and only two integer type data
"""


def add_integer(a, b=98):
    """ A simple function to add two integers"""
    """testing 'a' datatype"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    """testing 'b' datatype"""
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a)+int(b)
