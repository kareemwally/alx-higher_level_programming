#!/usr/bin/python3
import json
"""
simple function to get the JSON representation
"""


def to_json_string(my_obj):
    """using dumps method"""
    res = json.dumps(my_obj)
    return res
