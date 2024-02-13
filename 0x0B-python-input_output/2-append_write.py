#!/usr/bin/python3
"""
a simple function to append sentence to a file
"""


def append_write(filename="", text=""):
    """using with statement to append"""
    with open(filename, 'a', encoding='utf-8') as A:
        print("{}".format(text), end="", file=A)
    return len(text)
