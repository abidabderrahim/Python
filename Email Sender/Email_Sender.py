"""
Python tool for sending email .
"""

from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'my_email@gmail.com'
email_password_app = '*'

email_receiver = 'other_email@gmail.com'

subject = "Hello World!"
body = """
this first message from python email sending tool .
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password_app)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
