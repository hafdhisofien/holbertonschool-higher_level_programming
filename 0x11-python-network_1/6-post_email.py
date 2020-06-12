#!/usr/bin/python3
"""
Python script that sends a POST request to the passed
URL with the email as a parameter,
and finally displays the body of the response.
"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)
