#!/usr/bin/python3
"""
simple function to get the JSON representation
"""


import json


def to_json_string(my_obj):
    """using dumps method"""
    res = json.dumps(my_obj)
    return res
