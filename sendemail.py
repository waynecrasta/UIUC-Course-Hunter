import smtplib
from passwords import details


def sendEmail():
    sender = details['email']
    password = details['password']
    recipient = details['recipient']
    subject = 'Your course is open'
    body = 'happy registration :)'
    message = 'Subject: %s\n\n%s' % (subject, body)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, message)
    server.quit()
