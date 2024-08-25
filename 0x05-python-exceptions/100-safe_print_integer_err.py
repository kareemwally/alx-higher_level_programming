#!/usr/bin/python3


def safe_print_integer_err(value):
    """simple function to print integrs"""
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as e:
        print(e)
        return False
    return True
