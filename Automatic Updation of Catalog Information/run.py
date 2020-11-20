#! /usr/bin/env python3
import os
import requests
for file in os.listdir("/home/student-02-b6e027a30c35/supplier-data/description$
        feed={}
        with open("/home/student-02-b6e027a30c35/supplier-data/descriptions/"+file) as f:
                line=f.readlines()
                feed["name"]=line[0].strip()
                feed["weight"]=int(line[1][:line[1].index(" ")].strip())
                feed["description"]=line[2].strip()
                feed["image_name"]="/home/student-02-b6e027a30c35/supplier-data/images/"+file[:file.index(".")]+".jpeg"
                f.close()
        res=requests.post("http://104.197.243.64/feedback/?format=",data=feed)
        print(feed)
