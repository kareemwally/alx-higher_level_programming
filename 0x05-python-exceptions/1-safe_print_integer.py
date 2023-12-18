#!/usr/bin/python3
def safe_print_integer(value):
    try:
        res = int(value)
        print("{:d}".format(res))
        return True
    except ValueError:
        return False
