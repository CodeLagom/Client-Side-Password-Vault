import smtplib
import pyotp
import time

totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
otp=totp.now();
myotp = str(otp)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("papalipratap@gmail.com", "saswat@1998")
server.sendmail("papalipratap@gmail.com", "rickrudra@gmail.com", 'your otp is ' + myotp)
time.sleep(15)
otp=""
