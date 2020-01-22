#!/usr/bin/python3
import json
"""
importing JSON functions
"""


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
    Args:
    filename: current file name.
    Returns: object that we created.
    """
    with open(filename) as f:
        return json.load(f)
