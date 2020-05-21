#! python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:55:28 2020

@author: SiddharthPatra
"""



import webbrowser,sys,pyperclip

#web1 = webbrowser.open('https://google.com') 
#print(web1)#prints true, also opens microsoft edge and goes to the link given


''' What if we could automate certain web tasks? 
For example, if we did the run command in windows and performed: 'mapit.py Valencia Street'
See mapit.py
'''
sys.argv # ['mapit.py', 'address', 'split', 'by', 'space', 'here']

if len(sys.argv) > 1: # if address to search is on command
    address = ' '.join(sys.argv[1:])
else:
    address = '316 West Beaver Avenue, State College'

#for mapit.py, all we have to do is go to a link like:
    #https://www.google.com/maps/place/+address_here
webbrowser.open('https://www.google.com/maps/place/'+address)