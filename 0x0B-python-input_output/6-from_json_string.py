#!/usr/bin/python3
import json
"""
importing JSON functions
"""


def from_json_string(my_str):
    """
    function that returns an object (Python data structure)
    represented by a JSON string
    Args:
    my_str: string to parse
    Returns: object represnted by JSON string
    """

    return json.loads(my_str)
