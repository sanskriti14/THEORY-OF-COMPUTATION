# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:40:34 2019

@author: Sanskriti
"""

def flip(c):
    return '1' if (c == '0') else '0'

def getComplement(n):
    l = len(n) 
    ones = ""
    twos = ""
    for i in range(l):
        ones += flip(n[i]) 
  
    ones = list(ones.strip(""))
    twos = list(ones)
    for i in range(l - 1, -1, -1):
        if (ones[i] == '1'):
            twos[i] = '0'
        else:      	
            twos[i] = '1'
            break
    if (i == -1):
        twos.insert(0, '1') 
  
    print("1's complement: ", *ones)
    print("2's complement: ", *twos)
      
if __name__ == '__main__':
    t=int(input("Enter no. of Test Cases : "))
    while t>0:
        t=t-1
        n = input("Enter a binary number : ")
        getComplement(n)
