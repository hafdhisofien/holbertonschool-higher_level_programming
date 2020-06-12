#!/usr/bin/python3
"""
Python script that takes your Github credentials
(username and password) and uses the Github API to display your id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    response = requests.get('https://api.github.com/user',
                            auth=(argv[1], argv[2]))
    try:
        print(response.json().get("id"))
    except KeyError:
        print("None")
