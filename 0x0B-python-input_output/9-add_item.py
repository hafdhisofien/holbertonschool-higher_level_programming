#!/usr/bin/python3
from sys import argv
""" import the argv function  """

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
""" import our save function """

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
""" import our load function """

filename = "add_item.json"
try: 
    data = load_from_json_file(filename)
    data += argv[1:]
    save_to_json_file(data, filename)
except FileNotFoundError:
    data = argv[1:]
    save_to_json_file(data, filename)
