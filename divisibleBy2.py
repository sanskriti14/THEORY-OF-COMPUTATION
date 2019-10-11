# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:52:26 2019

@author: Sanskriti
"""

t=int(input("Enter no. of Test Cases : "))
while t>0:
	t=t-1
	s=int(input("Enter a String : "))
	if(s%2==0):
		print("String Accepted")
	else:
		print("String Rejected")
