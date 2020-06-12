#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        print("[{}] {}".format(response.json()['id'], response.json()['name']))
    except ValueError:
        print("Not a valid JSON")
    except:
        print("No result")
