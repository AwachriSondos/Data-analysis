# Disable wannings
import os
import warnings
warnings.simplefilter(action = 'ignore', category=FutureWarning)
warnings.filterwarnings('ignore')
def ignore_warn(*args, **kwargs):
    pass

#Import libraries
import os
import glob
import errno
from datetime import datetime, date
import pandas as pd
import numpy as np
from collections import Counter

import imaplib
import base64
import email

import random

#Read mails, extract joint files

email_user = input('Email: ')
email_pass = input('Password: ')


# login and set gmail directory
mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
mail.login(email_user, email_pass)
mail.select('Inbox')


#Get the mails contents

type, data = mail.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.split()

for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
# converts byte literal to string removing b''
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
# downloading attachments
    for part in email_message.walk():
        # this part comes from the snipped I don't understand yet... 
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join('/Users/sanketdoshi/python/', fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
            subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
             print('Downloaded "{file}" from email titled "{subject}" with UID {uid}.'.format(file=fileName, subject=subject, uid=latest_email_uid.decode('utf-8')))


#print the mail content

for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1].decode('utf-8'))
            email_subject = msg['subject']
            email_from = msg['from']
            print ('From : ' + email_from + '\n')
            print ('Subject : ' + email_subject + '\n')
            print(msg.get_payload(decode=True))


#unzip files

import zipfile
with zipfile.ZipFile('$path$/Timeline.zip', 'r') as zip_ref:
    zip_ref.extractall('$path$')

