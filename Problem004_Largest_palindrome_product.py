# -*- coding: utf-8 -*-
# Problem 004 Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import time

def is_palindrome(nbr) :
    nbr=list(str(nbr))
    l=len(nbr)
    for i in range(l) :
        if nbr[i] != nbr[-i-1] :
            return False
    return True

p=1
for i in range(1,1000) :
    for j in range (1000//p,1000) :
       if is_palindrome(i*j) and i*j>p :
           p=i*j
           L=[i,j,p]
print(L)
