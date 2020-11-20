'''
The main objective is to write script to process images using PIL module
'''
#!/usr/bin/env python3
from PIL import Image
import os
for file in os.listdir("/home/student-02-89a54122e313/images"):
        if not file.startswith("."):
                im=Image.open("/home/student-02-89a54122e313/images/"+file).convert("RGB")
                im.rotate(90).resize((128,128)).save("/opt/icons/"+file+".jpeg")

