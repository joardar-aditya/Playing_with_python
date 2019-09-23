#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 00:27:54 2019

@author: jordan
"""

#! python3
#importing modules
import pyperclip, re
#creating the phone regex
phoneregex = re.compile(r'((\d*|\(\d*\))?(\s|-|\.)?(\d{7,10}))')

#creating the email regex

emailRegex = re.compile(r'\w+@{1}\w+\.\w+\.*\w+')
#Finding all the matches in clipboard text
#TODO:
#Obtaining the text from the clipboard


text = str(pyperclip.paste())
matches_ph = phoneregex.findall(text)
matches_email = emailRegex.findall(text)



#Displaying the result
#TODO: 

