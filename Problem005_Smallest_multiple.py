# -*- coding: utf-8 -*-
# Problem 005 Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import time

start=time.time() 
nbr=1
for j in range(1,20) :
    i=1
    n=nbr
    while n%j != 0 :
        n=nbr*i
        i=i+1
    nbr=n
print(nbr)    
end=time.time()
print(f"temps pour trouver la réponse : {end-start}")