#!/usr/bin/python3
import json
"""
importing JSON functions
"""

def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation
    Args:
    my_obj:object to be written.
    filename: current file name.
    Returns: none.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
