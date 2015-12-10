# coding: utf8

__author__ = 'mikelrob'

from selenium.webdriver.common.by import By
from selenium import webdriver

PEOPLE = ('Michael Robinson',
          'Matt Dickinson',
          'Jonny Moore',
          'Andrew Shannon',
          'Phil Stevenson',
          )

driver = webdriver.Firefox()
footy_url = "http://teamfinder.org/games/98ca528424dc679d0901"
driver.get(footy_url)

title1 = "Team Finder"
title2 = "Tuesday Night Football"

assert title1 in driver.title
assert title2 in driver.title

elements = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/table/tbody/tr")

for elem in elements:
    for name in PEOPLE:
        if name in elem.text:
            print "Found {0}".format(name)
            tds = elem.find_elements_by_tag_name('td')
            for td in tds:
                if 'Yes' in td.text:
                    radio_input = td.find_element_by_tag_name('input')
                    radio_input.click()
                    print "Clicked Yes"

driver.close()



# def send_email():
#             import smtplib
#
#             gmail_user = "user@gmail.com"
#             gmail_pwd = "secret"
#             FROM = 'user@gmail.com'
#             TO = ['recepient@mailprovider.com'] #must be a list
#             SUBJECT = "Testing sending using gmail"
#             TEXT = "Testing sending mail using gmail servers"
#
#             # Prepare actual message
#             message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
#             """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
#             try:
#                 #server = smtplib.SMTP(SERVER)
#                 server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
#                 server.ehlo()
#                 server.starttls()
#                 server.login(gmail_user, gmail_pwd)
#                 server.sendmail(FROM, TO, message)
#                 #server.quit()
#                 server.close()
#                 print 'successfully sent the mail'
#             except:
#                 print "failed to send mail"
