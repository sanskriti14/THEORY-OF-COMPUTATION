# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:23:10 2019

@author: Sanskriti
"""

t=int(input("Enter no. of Test Cases : "))
while t>0:
    t=t-1
    str1=input("Enter first string : ")
    str2=input("Enter second string : ")
    if(sorted(str1)==sorted(str2)):
        print("Both the strings are Anagrams")
    else:
        print("Both the strings are Not Anagrams")