import smtplib
import getpass

sender = input('Enter sender email address: ')
receiver = input('Enter receiver email address: ')
try:
    password = getpass.getpass(prompt="Enter sender's email login password: ", stream=None)
except Exception as error:
    print('ERROR', error)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login(sender, password)

# message to be sent
message ="""
Hey,

    How are you today?

Regards,
Dhruv

**Sent from Python!**
"""
s.sendmail(sender, receiver, message)
s.quit()
