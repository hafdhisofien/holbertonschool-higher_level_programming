#!/usr/bin/python3
"""
Python script sends a request to the URL and displays the body of the response
"""
import urllib
from urllib import request
from urllib import error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as r:
            response = r.read()
            print(response.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
