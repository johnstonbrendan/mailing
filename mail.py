import email
import smtplib
import names
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#username tt0370464
#password tt03704641234
#s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s = smtplib.SMTP(host='smtp.gmail.com', port=587)

from string import Template

s.starttls()
s.login("tt0370464", "tt03704641234") #need to make own email
n = 100 #number of times
msg = MIMEMultipart()       # create a message
for i in range (n):
    reciever = names.get_full_name()
    sender = names.get_full_name()
    recieve_address = "tt0370464@gmail.com"
    msg = MIMEMultipart()       # create a message

    # setup the parameters of the message
    msg['From']=sender
    msg['To']= recieve_address
    msg['Subject']="Bottles of beer"
    if n-i == 2:
        body = "1 Bottle of beer on the wall, 1 bottle of beer.\n"
        body = body + "Take it down and pass it around, no bottles of beer on the wall."
    elif n-i == 1:
        body = str(n-i-1) + " Bottles of beer on the wall, " + str(n-i-1) + " bottles of beer.\n"
        body = body+ "You go to the store to find some more, and you find 99 bottles of beer on the wall."
    else:
        body = str(n-i-1)+" Bottles of beer on the wall, " + str(n-i-1) + " bottles of beer.\n"
        body = body + "Take one down and pass it around, " + str(n-i-2) + " bottles of beer on the wall."
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        # send the message via the server set up earlier.

        s.sendmail(sender,recieve_address, text)
        print (text)
        del msg
