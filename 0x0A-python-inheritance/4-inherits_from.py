#!/usr/bin/python3
"""
function to check the base or inherited class
"""


def inherits_from(obj, a_class):
    """using issubclass method"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
