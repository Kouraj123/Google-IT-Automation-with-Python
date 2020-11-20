'''
The objective is to write script which interacts with web service capable of storing and displaying the reviews of company.
Internally the reviews are stored in text files, process the information into the specified format and sends the result to web service to store the result
'''
#!/usr/bin/env python3
import os
import requests
for file in os.listdir("/data/feedback"):
        feed={}
        with open("/data/feedback/"+file) as f:
                line=f.readlines()
                feed["title"]=line[0].strip()
                feed["name"]=line[1].strip()
                feed["date"]=line[2].strip()
                feed["feedback"]=line[3].strip()
                f.close()
        res=requests.post("http://104.197.243.64/feedback/?format=",data=feed)
        print(res.status_code)
