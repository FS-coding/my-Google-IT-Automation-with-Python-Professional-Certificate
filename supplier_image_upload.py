#! usr/bin/env python3
import requests
import os

url = "http://localhost/upload"
source = "~/supplier-data/images/"
files = os.listdir(source)

for file in files:
    with open(file, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
