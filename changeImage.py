#!/usr/bin/env python3

import os
from PIL import Image

user = os.getenv('USER')
old_path = "/home/{}/~/supplier-data/images".format(user)
# just in case save directory is different
new_path = "/home/{}/~/supplier-data/images/".format(user)

files = os.listdir(old_path)
# os.chdir(old_path)

for file in files:
    with Image.open(old_path + file) as im:
        im.convert('RGB')
        # im.rotate(-90)
        im.resize((600, 400))
        im.save(new_path + file, "JPEG")
        im.close()
