# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:49:28 2019

@author: Sanskriti
"""

t=int(input("Enter no. of Test Cases : "))
while t>0:
	t=t-1
	s=input("Enter a String : ")
	if(len(s)>=3):
		if(s[-1]=='1' and s[-2]=='0' and s[-3]=='1'):
			print("String Accepted")
		else:
			print("String Rejected")
	else:
		print("Length should be greater than 2")
