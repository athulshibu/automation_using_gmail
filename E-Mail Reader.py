import smtplib
import imaplib
import imapclient
import pyzmail
import os



ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "remoteaccesautomation" + ORG_EMAIL
FROM_PWD    = "spamandeggs"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(FROM_EMAIL,FROM_PWD)

imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['ALL'])
latest_email_id = int(UIDs[-1])
#print(UIDs)
#print(latest_email_id)

rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
message = pyzmail.PyzMessage.factory(rawMessages[latest_email_id][b'BODY[]'])
#print('\nSUBJECT: ' + message.get_subject() + '\n\n')


if message.text_part != None:
    #print(message.text_part.get_payload().decode(message.text_part.charset))
    #command = "os.startfile(message.text_part.get_payload().decode(message.text_part.charset)[:-2])"
    exec(message.text_part.get_payload().decode(message.text_part.charset)[:-2])

imapObj.logout()
