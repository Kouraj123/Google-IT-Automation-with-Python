#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
for file in os.listdir("/home/student-02-b6e027a30c35/supplier-data/images"):
        if file.endswith(".jpeg"):
                with open("/home/student-02-b6e027a30c35/supplier-data/images/"+file, 'rb') as opened:
                        r = requests.post(url, files={'file': opened})

