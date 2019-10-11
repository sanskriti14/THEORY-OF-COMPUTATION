# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:09:31 2019

@author: Sanskriti
"""

t=int(input("Enter no. of Test Cases : "))
while t>0:
    t=t-1
    s=input("Enter String : ")
    count0=0
    count1=0
    for i in s:
        if i=='0':
            count0=count0+1
    for x in s:
        if x=='1':
            count1=count1+1
    if(count0==count1):
        print("There are equal number of 0's and 1's.")
    else:
        print("There are unequal number of 0's and 1's.")

        
        