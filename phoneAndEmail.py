# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:58:08 2020

@author: SiddharthPatra
"""


#! python3
import re, pyperclip#pyperclip for copying and pasting

#TODO: Create a regex for phone numbers

phoneRegex = re.compile(r''' (
# Comments - what kind of numbers are we collecting?
# 415-555-0000 (full number), 555-0000 (no area code), (415) 555 0000 
#   (no spaces, parentheses around area code), 555-0000 ext 12345 (extension 
#   handling), ext. 12345 (extension without number), x12345 (another notation 
#   for extension)
((\d\d\d) | (\(\d\d\d\)))? # area code: Means either 3 digits, or 3 digits with 
#   parentheses. ? means optional.
(\s|-) # first separator: # Space or dash
\d\d\d # first 3 digits: 3 digits
- # separator: We can just assume the case to be a dash
\d\d\d\d # last 4 digits: 
(((ext(\.)?\s)|x) # extension (optional): 
 (\d{2,5}))? #extension number-part (optonal)
# Extension is made up of 'ext' or 'x', followed by 2-5 digits. 
#   The 'ext' part is optional, and the whole thing is optional.
) #1st and last parentheses takes number as a single thing
''', re.VERBOSE)


#TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
#Comments - what is the format of an email address?
# some._+_thing@(\d{2,5})?.com
[a-zA-Z0-9_.+]+ # this is the name part
@ #@ symbol
.[a-zA-Z0-9_.+]+ # domain name
                        ''', re.VERBOSE)

#TODO: Extract the email/phone from this text

text = pyperclip.paste()

#TODO: Copy extracted email/phone to the clipboard
extractedPhone = phoneRegex.findall(text)
#findall returns a list of tuples with each having several strings
allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0]) # contains all first strings in list of tuples
#print(extractedPhone)
print(allPhoneNumbers)
extractedEmail = emailRegex.findall(text)
#findall returns a list of strings
print(extractedEmail)


results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
# pyperclip.copy(results) #copies all copied phone numbers and email addresses