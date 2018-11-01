#! /usr/bin/python

import os
import getpass
import paramiko
#import xlsxwriter
import socket
import  re
import sys
import smtplib
#from email import encoders
#from email.mime.multipart import MIMEMultipart
#from email.mime.base import MIMEBase
#from email.MIMEText import MIMEText



username = raw_input('Enter username for device login:')

def enterPassword():
  while True: # repeat forever
    password = getpass.getpass('Enter corresponding password:')
    password_again = getpass.getpass('Confirm password:')
    if password != password_again:
      print ('Password and confirmation do not match.Please try again!!')
    else:
      return password
password = enterPassword()

recipient = raw_input('Enter your email-id where the results of the test will be mailed to you :')
sender = raw_input('Enter recipient email address: ')
subject = raw_input('Enter subject for the mail: ')
message = raw_input('Enter the message body:')
SMTP_SERVER = raw_input('Enter SMTP server FQDN:')
SMTP_PORT = 587
print ("Running the tests..this might take some time..")

# Opens file in read mode
f1 = open('hostfile','r')
f2 = open('commandfile','r')
# Creates list based on f1
devices = f1.readlines()
commands = f2.readlines()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

data = []
for device in devices:
        column = device.split()
        data.append([column[0]])
        print( column[0])
        for command in commands:
            try:
                    conn=ssh.connect(column[0], username=username, password=password, timeout=4)
                    if conn is None:
                        stdin, stdout, stderr = ssh.exec_command(command)
                        data[-1].append(stdout.read())
                        ssh.close()
            except  paramiko.AuthenticationException:
                    output = "Authentication Failed"
                    data[-1].append(output)
                    break
            except  paramiko.SSHException:
                    output = "Issues with SSH service"
                    data[-1].append(output)
                    break
            except  socket.error:
                    output = "Connection Error"
                    data[-1].append(output)
                    break
        data[-1] = tuple(data[-1])


f1.close()
f2.close()
