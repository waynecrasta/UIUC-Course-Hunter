import smtplib
from passwords import details


def sendEmail(message):
    sender = details['email']
    password = details['password']
    recipient = details['recipient']
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, message)
    server.quit()
