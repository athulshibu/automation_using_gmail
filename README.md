# automation_using_gmail

****Selenium for Python****
from selenium import webdriver
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("**website**")
searchbar = driver.find_element_by_name("**q**") #finding searchbar
searchbar.send_keys(**epiname**) #send text into searchbar
#Use Inspect Element in browser to find link_text, id, xpath etc.
episode = driver.find_element_by_link_text("Watch Detective Conan - 917 Online")
episode.click()
episodeno = driver.find_element_by_id("episodeMenu")
episodeno.click()
episode = driver.find_element_by_link_text(epinum)
episode.click()
provider = driver.find_element_by_id("providerMenu")
provider.click()
provider = driver.find_element_by_xpath("//button[@data-provider='mp4upload']")
provider.click()
episodedets = driver.find_elements_by_xpath("//button[@data-resolution='720p']")
episodedets.click()


****Reading from G-Mail****
**** For Reference : https://automatetheboringstuff.com/chapter16/****
import smtplib
import time
import imaplib
import email
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
    #print(message.text_part.get_payload().decode(message.text_part.charset)) # To just print the mail
    #command = "os.startfile(message.text_part.get_payload().decode(message.text_part.charset)[:-2])"
    exec(message.text_part.get_payload().decode(message.text_part.charset)[:-2]) # Execute the command sent by mail

imapObj.logout()
