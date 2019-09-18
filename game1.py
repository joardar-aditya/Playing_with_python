#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:19:28 2019

@author: jordan
"""

import random
secretnumber = random.randint(1,200)
print("I am thinking of a number between 1 and 20")

for guesses in range(1,7):
    print("Enter your Guess")
    guess = int(input())
    if(guess==secretnumber):
        print("Wow! your guess is correct!")
        break
    elif(guess<secretnumber):
        print("Guess too low, try again")
    elif(guess>secretnumber):
        print("Guess too high, try again")
if(guess!=secretnumber):
    print("Sorry! you're out of luck!" + str(secretnumber))