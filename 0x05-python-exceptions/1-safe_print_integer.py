#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if int(value) == value:
            print("{:d}".format(value))
            return True
    except (ValueError, TypeError):
        pass
    return False
