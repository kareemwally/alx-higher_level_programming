#!/usr/bin/python3
"""
a simple functio for printing Your Fname, Lname and fully tested
by different test cases
"""


def say_my_name(first_name, last_name=""):
    """
    obviousily only two args are give with optional last name arg
    """
    if type(first_name) is str:
        if type(last_name) is str:
            print("My name is {} {}".format(first_name, last_name))
        else:
            raise TypeError("last_name must be a string")
    else:
        raise TypeError("first_name must be a string")
