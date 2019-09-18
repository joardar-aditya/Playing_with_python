#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:06:39 2019

@author: jordan
"""
#Printing a list in a given format from the given list

given_list = list(map(str, input().split()))
string = ''
length = len(given_list)
for i in given_list:
    if(length > 2):
        string += i + ', '
    elif(length==2):
        string += i + ' and '
    else:
        string += i + '.'
    length -= 1
print(string)        
     