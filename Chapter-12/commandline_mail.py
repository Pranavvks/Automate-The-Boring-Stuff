
import sys
from selenium import webdriver
n=len(sys.argv)
if n<=1:
    print("Enter again")
    sys.exit()
else:
    emailid_user=''.join(sys.argv[1])
    string_data=''.join(sys.argv[2])
    browser=webdriver.Firefox()

    Website=browser.get('https://mail.google.com/mail/u/0/#inbox?compose=new')

    To=browser.find_element_by_id(':ma')
    final=To.send_keys(emailid_user)
    send=To.submit()
    
    Subject=browser.find_element_by_id(':ln')
    Subject_send=Subject.send_keys(string_data)
    Subject_done= Subject.submit()
