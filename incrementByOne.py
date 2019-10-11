# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 00:09:57 2019

@author: admin
"""

def incr(bit_string):
    carry = False
    bits = list(bit_string[::-1])
    for i, bit in enumerate(bits):
        carry = bit != "0"
        if bit == "0":
            bits[i] = "1"
            break
        else:
            bits[i] = "0"
    if carry:
        bits.append("1")
    return "".join(bits[::-1])

if __name__ == '__main__':
    t=int(input("Enter no. of Test Cases : "))
    while t>0:
        t=t-1
        n = input("Enter a binary number : ")
        print (incr(n))
