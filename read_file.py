# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 01:00:50 2020

@author: SiddharthPatra
"""

def readfile():
    txt = ""
    f = open("examplePhoneEmailDirectory.txt", "r")
    for x in f:
        txt+=x
        print(x)
    f.close()
    return txt

