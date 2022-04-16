import smtplib
from email.message import EmailMessage

with open('gmail.txt') as secretFile:
    USERNAME = secretFile.readline()
    PASSWORD = secretFile.readline()

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.ehlo()
        server.login(USERNAME, PASSWORD)

        msg = EmailMessage()
        msg.set_content('Testing Using email lib')
        msg['Subject'] = "There's a new problem"
        msg['From'] = 'Stephen Schleising <stephen@schleising.net>'
        msg['To'] = 'Stephen Schleising <stephen@schleising.net>'

        server.send_message(msg)
except:
    print('Something went wrong')
