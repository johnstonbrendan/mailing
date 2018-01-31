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

# def read_template(filename):
#     with open(filename, 'r', encoding='utf-8') as template_file:
#         template_file_content = template_file.read()
#     return Template(template_file_content)

s.starttls()
s.login("tt0370464", "tt03704641234")
reciever = "Benjamin Duo"
company = "Microsoft"
n = 100 #number of times#CHANGE THIS
# For each contact, send the email:
msg = MIMEMultipart()       # create a message
# message_template = read_template('message.txt')
sender = names.get_full_name()
for i in range (n):
    sender = names.get_full_name()
    recieve_address = "blduo@uwaterloo.ca"
    # add in the actual person name to the message template
    # message = message_template.substitute(PERSON_NAME="Ben Duo".title())
    msg = MIMEMultipart()       # create a message

    # setup the parameters of the message
    msg['From']=sender
    msg['To']= recieve_address
    msg['Subject']="%s Position" %(company)
    # msg.attach(MIMEText(message, 'plain'))
    # add in the message body


    body = "Dear %s,\nThank you for your interest in our application. We had many promising applicants to this program and have had to reject many qualified students. We felt that your skills would allow you to learn in our environment and would like to learn more about you." %(reciever)
    body = body + "\nPlease go into your WaterlooWorks account to confirm your interview time."
    body = body +"\n\nWe hope you strongly consider our position \nThanks\n%s" %(sender)
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    # send the message via the server set up earlier.

    s.sendmail("interviewsforstudents@gmail.com",recieve_address, text)
    print (text)
    del msg



# from string import Template
#
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# MY_ADDRESS = 'my_address@example.comm'
# PASSWORD = 'mypassword'
#
## def get_contacts(filename):
##     """
##     Return two lists names, emails containing names and email addresses
##     read from a file specified by filename.
##     """
##
##     names = []
##     emails = []
##     with open(filename, mode='r', encoding='utf-8') as contacts_file:
##         for a_contact in contacts_file:
##             names.append(a_contact.split()[0])
##             emails.append(a_contact.split()[1])
##     return names, emails
##
## def read_template(filename):
##     """
##     Returns a Template object comprising the contents of the
##     file specified by filename.
##     """
##
##     with open(filename, 'r', encoding='utf-8') as template_file:
##         template_file_content = template_file.read()
##     return Template(template_file_content)
##
# def main():
#     names, emails = get_contacts('mycontacts.txt') # read contacts
#     message_template = read_template('message.txt')
#
#     # set up the SMTP server
#     s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
#     s.starttls()
#     s.login(MY_ADDRESS, PASSWORD)
#
#     # For each contact, send the email:
#     for name, email in zip(names, emails):
#         msg = MIMEMultipart()       # create a message
#
#         # add in the actual person name to the message template
#         message = message_template.substitute(PERSON_NAME=name.title())
#
#         # Prints out the message body for our sake
#         print(message)
#
#         # setup the parameters of the message
#         msg['From']=MY_ADDRESS
#         msg['To']=email
#         msg['Subject']="This is TEST"
#
#         # add in the message body
#         msg.attach(MIMEText(message, 'plain'))
#
#         # send the message via the server set up earlier.
#         s.send_message(msg)
#         del msg
#
#     # Terminate the SMTP session and close the connection
#     s.quit()
#
# if __name__ == '__main__':
#     main()
