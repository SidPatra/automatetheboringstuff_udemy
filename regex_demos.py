# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:31:58 2020

@author: SiddharthPatra
"""
import read_file
''' VIDEO 1 '''
'''NON-REGEX DEMO FOR PHONE NUMBER DETECTION
    Just to figure out the logic first'''
def isPhoneNumber(text):
    if len(text)!=12:
        return False #not phone # size
    for i in range(0,7):
        if not text[i].isdecimal() and i!=3:
            return False #no area code
    if (text[3]!='-' or text[7]!='-') and (text[3]!=' ' or text[7]!=' '):#- is accounted for
        return False #missing at least one dash
    return True
print("NON-REGEX RESULT")
print(isPhoneNumber('415-555-1234'))#True
print(isPhoneNumber('hello'))#False

message = 'Call me on 415-555-1234 tomorrow, or at 415-555-9999'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found:',chunk)
        foundNumber = True
if not foundNumber:
    print("No phone numbers found")
print("/n/n")
'''REGEX PART STARTS NOW'''
import re

print("REGEX POINT 1: NUMBER DETECTION")
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #raw strings passed through to this
#\d for every location where there is a number, dash where is a dash
numfound = phoneNumRegex.search(message)#this is a re.Match object with a span and match result
print("Phone number found:",numfound.group())
numlst = phoneNumRegex.findall(message)#puts every number found into a list
print("All numbers found:",numlst)

'''VIDEO 2'''
#(\d\d\d)-(\d\d\d-\d\d\d\d): this separates the phone number into 2 parts, lets
# you separate the area code and the rest of the number.
print("REGEX POINT 2: MORE THAN ONE NUMBER")
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #raw strings passed through to this
numlst = phoneNumRegex.findall(message)#puts every number found into a list
print("All numbers found:",numlst) #outputs list of 2 tuples of 2 strings each.
#Output is: [('415', '555-1234'), ('415', '555-9999')]

print("REGEX POINT 3: BATREGEX PIPE")
# point of this one is to learn about the pipe '|' character/operator.
batregex = re.compile(r'Bat(man|mobile|copter|bat)')
batty = batregex.search('Batmobile lost a wheel')
print(batty.group())
batty = batregex.search('Batmotorcycle lost a wheel')
print(batty==None) #will return true, bc Batmotorcycle not recognized
#mo.group() will also return an error

'''VIDEO 3'''
print("REGEX POINT 4: PATTERNS AND GREEDY/NONGREEDY MATCHING")
#what happens if you want to see if something appears more than 7 times but less than 10 times?
batty = re.compile(r'Bat(wo)?man')
batresults = batty.search('The Adventures of Batman')
print(batresults.group())
batresults = batty.search('The Adventures of Batwoman')
print(batresults.group())
batresults = batty.search('The Adventures of Batwowowowowman')
print(batresults==None)#prints True
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.').group())
#above prints the whole phone number
print(phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')==None)
#above prints True
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
print(phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.'))
#above prints the re.Match object for whole phone number
print(phoneRegex.search('My phone number is 555-1234. Call me tomorrow.'))
#above prints the re.Match object for just last 7 digits (not area code)
#PUTTING QUESTION MARK: means expression preceding questionmark is optional
#To find mentions of string 'dinner?', we do re.compile(r'dinner\?')
# In that case, dinner is not optional, we're literally looking for a '?'
print("REGEX POINT 5: * CHARACTER")
batty = re.compile(r'Bat(wo)*man') #checks for any number of 'wo' chars
#(wo)* means any number of mentions of 'wo'. Any number means 0 of it, or more.
batresults = batty.search('The Adventures of Batman')
print(batresults.group())
batresults = batty.search('The Adventures of Batwoman')
print(batresults.group())
batresults = batty.search('The Adventures of Batwowowowoman')
print(batresults.group())
print("REGEX POINT 6: + CHARACTER")
#What if we want at least one 'wo'
batty = re.compile(r'Bat(wo)+man')
batresults = batty.search('The Adventures of Batman')
print(batresults) #prints None
batresults = batty.search('The Adventures of Batwoman')
print(batresults)
batresults = batty.search('The Adventures of Batwowowowoman')
print(batresults)

print("REGEX POINT 7: REPEATING PATTERNS + GREEDINESS")
#What if you want to find patterns like '+*?'
regex = re.compile(r'\+\*\?')
print(regex.search('I learned about the +*? regex syntax'))
regex = re.compile(r'(\+\*\?)+') #what if you want to find more than one of that pattern?
print(regex.search('I learned about the +*?+*?+*?+*?+*?+*? regex syntax'))
haRegex = re.compile(r'(Ha){3}')#{3} means exactly 3 'Ha's or more in a row
print(haRegex.search('He said "HaHaHa"'))#3 or more 'Ha's results in a match
print(haRegex.search('He said "HaHa"'))#only 2, so no match
print(haRegex.search('He said "HaHaXHaHa"'))
#above, there is 4, but not in a row, so no match. if no 'X' char, then works
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}') #expects at least 3 phone numbers, maybe separated by commas
print(phoneRegex.search('My numbers are 415-555-1234,415-555-9999,415-999-1124'))
print(phoneRegex.search('My numbers are 415-555-1234415-555-9999415-999-1124'))
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,|.)?){3}') #expects at least 3 phone numbers, maybe separated by commas
print(phoneRegex.search('My numbers are 415-555-1234.415-555-9999.415-999-1124'))
haRegex = re.compile(r'(Ha){3,5}')#{3,5} means at most finds group of 5 'Ha's.
#{3,} == {3} same functionality
#{3,5} is inclusive, like [3,5], not (3,5)
print(haRegex.search('He said "HaHaHa"'))#minimum
print(haRegex.search('He said "HaHaHaHaHaHa"'))#past the max
print(haRegex.search('He said "HaHa.HaHa.HaHa"'))#more than 6, but not in a row so None
digitRegex = re.compile(r'(\d){3,5}') #greedy match - longest string possible
print(digitRegex.search('1234567890'))
print(digitRegex.findall('1234567890'))
digitRegex = re.compile(r'(\d){3,5}?')#nongreedy match - shortest string possible, done with '?' after {}
print(digitRegex.search('1234567890'))
print(digitRegex.findall('1234567890'))

'''VIDEO 4'''
print("REGEX POINT 8: FINDALL")
pdf_file = readfile()
#pdf_re = re.compile(pdf_file)
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')#finds full phone #s
print("All numbers found-1",len(phoneRegex.findall(pdf_file)))#719 elements
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')#finds tuples of area code and rest of the number
print("All numbers found-2",len(phoneRegex.findall(pdf_file)))#719 elements with each element being tuple of size 2
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')#finds tuples of area code, rest of number, and full number
print("All numbers found-3",len(phoneRegex.findall(pdf_file)))#719 elements with each element being tuple of size 3

lyrics = "12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree"
xmasRegex = re.compile(r'\d+\s\w+')
#at least one number, one space-like character, at least one character/string
print(xmasRegex.findall(lyrics)) #breaks up the song lyrics

print('REGEX POINT 9: MAKING YOUR OWN CHARACTER CLASSES')
vowelRegex = re.compile(r'[aeiou]')#all vowels - same as (a|e|i|o|u)
vowelRegexCaps = re.compile(r'[aeiouAEIOU]')#all vowels including caps
allLettersRegex = re.compile(r'[a-zA-Z]')#hopefully all chars capital or lowercase, a-z means all letters from lowercase a to z
print(vowelRegex.findall('Robocop eats baby food.')) #gets all vowels (not uniquely, repeats exist)
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall('Robocop eats baby food.')) #gets all pairs of vowels like oo, ee, etc.
print(allLettersRegex.findall(lyrics)) #finds all characters in lyrics

print('REGEX POINT 10: NEGATIVE CHARACTER CLASSES')
consonantRegex = re.compile(r'[^aeiouAEIOU\s\d]')
print(consonantRegex.findall(lyrics))#finds everything that isn't a vowel, number or other character