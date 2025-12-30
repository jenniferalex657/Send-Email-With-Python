import smtplib
from email.mime.text import MIMEText
import logging

# Set up logging
logging.basicConfig(
    filename='email_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Email setup
sender = 'sender@gmail.com'
receiver = 'receiver@gmail.com' 
subject = 'Test Email'
body = 'Hello from Python!'
password = '**** **** **** ****' #create a password through Gmail.com

# Create the message
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.send_message(msg)
    logging.info('Email successfully sent to %s', receiver)
except Exception as e:
    logging.error('Failed to send email: %s', e)
