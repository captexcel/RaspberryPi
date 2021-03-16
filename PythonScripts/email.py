#!/usr/bin/env python3
# Email Handler
# Author: CaptExcel
import smtplib
import imghdr
from email.message import EmailMessage

user = "YOUR-GMAIL-ACCOUNT"
password = "YOUR-GOOGLE-2FA-AUTH-CODE" #Comment out to debug
    
def email_alert(subject, body, to, ipath):
    image_path = ipath
    
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user
    with open(image_path, 'rb') as fp:
        image_data = fp.read()
        image_type = imghdr.what(fp.name)
        image_name = fp.name
    msg.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
#    password = input('Password: ') #Remove comment to debug
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    #This will send a test email to the current user if the file is opened directly.
    email_alert("Testing", "This is a test", user, "")
