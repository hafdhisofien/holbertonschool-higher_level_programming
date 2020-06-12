#!/usr/bin/python3
"""
Python script to display the request-id in the header
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as r:
        response = r.info()
        print(response["X-Request-Id"])
