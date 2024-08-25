#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """simple function to print integrs"""
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as e:
        sys.stderr.write(e)
        return False
    return True
