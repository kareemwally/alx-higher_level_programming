#!/usr/bin/python3
"""
a simple function to write a sentence into a file
"""


def write_file(filename="", text=""):
    """using with statement"""
    with open(filename, 'w', encoding='utf-8') as W:
        print("{}".format(text), end='', file=W)
    return len(text)
