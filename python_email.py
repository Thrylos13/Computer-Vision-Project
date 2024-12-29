import smtplib
sender = str(input("Enter your email address:"))
receiver = str(input("Enter receiver's email address:"))
password = "cwjh bjhv mgpd srnq"
subject = "Test email"
body = "This email was sent to you via a python script, if you received it then acknowledge it back on whatsapp"

message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
try:
    server.login(sender,password)
    print("Logged in successfully")
    server.sendmail(sender, receiver, message)
    print("Email sent successfully")

except smtplib.SMTPAuthenticationError:
    print("Unable to sign in!")