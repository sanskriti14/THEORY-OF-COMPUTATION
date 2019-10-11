# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:26:45 2019

@author: Sanskriti
"""

t=int(input("Enter no. of test cases : "))
while t>0 :
    t=t-1
    s=input("Enter a string : ")
    c=0
    if(len(s)>=3):
        for i in range(len(s)-2):
            if(s[i]=='1' and s[i+1]=='1' and s[i+2]=='1'):
                c=1
                break
            else:
                c=0
    if(len(s)<3):
        print("Length should be greater than 2")
    elif(c==0):
        print("String Rejected")
    elif(c==1):
        print("String Accepted")
                    