#!/usr/bin/python3
import json

"""
importing Json functions
"""


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object (string)
    Args:
    my_obj: object (string) to be put in JSON format
    Returns: json object
    """
    return (json.dumps(my_obj))
