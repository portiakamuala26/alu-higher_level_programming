#!/usr/bin/python3
"""Sends a POST request with an email parameter."""

import sys
import urllib.parse
import urllib.request


data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")

with urllib.request.urlopen(sys.argv[1], data=data) as response:
    print(response.read().decode("utf-8"))
