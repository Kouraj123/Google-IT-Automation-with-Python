#!/usr/bin/env python3
from PIL import Image
import os
for file in os.listdir("/home/student-02-b6e027a30c35/supplier-data/images"):
        if file.find("LICENSE")<0 and file.find("README")<0:
                im=Image.open("/home/student-02-b6e027a30c35/supplier-data/images/"+file).convert("RGB")
                im.resize((600,400)).save("/home/student-02-b6e027a30c35/supplier-data/images/"+file[:-5]+".jpeg")



