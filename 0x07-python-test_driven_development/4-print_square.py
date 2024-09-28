#!/usr/bin/python3
"""
a simple function for printing Square withe the # character
by different test cases
"""


def print_square(size):
    """
    obviousily only one arg indicating the size of the square are give with
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    else:
        if size < 0:
            raise ValueError("size must be >= 0")
        for i in range(size):
            print('#'*size)
