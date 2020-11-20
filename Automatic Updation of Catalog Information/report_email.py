#!/usr/bin/env python3
import os
import datetime
import reports
import emails
if __name__=="__main__":
        title=""
        paragraph=""
        for file in os.listdir("/home/student-02-b6e027a30c35/supplier-data/descriptions"):
                title="Processed Update on "+datetime.datetime.now().strftime("%B %d,%Y")+"<br/><br/>"
                with open("/home/student-02-b6e027a30c35/supplier-data/descriptions/"+file) as f:
                        line=f.readlines()
                        paragraph+="name: "+line[0].strip()+"<br/>"+"weight: "+line[1].strip()+"<br/><br/>"
        reports.generate_report("/tmp/processed.pdf",title,paragraph)
        sender="automation@example.com"
        receiver="student-02-b6e027a30c35@example.com"
        subject="Upload Completed - Online Fruit Store"
        body="All fruits are uploaded to our website successfully. A detailed list is attached to this email."
        message=emails.generate_email(sender,receiver,subject,body,"/tmp/processed.pdf")
        emails.send_email(message)
