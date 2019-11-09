# -*- coding: utf-8 -*-
# Problem 007 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import time

start=time.time()
L=[2]
compteur = 1
nbr = 3
while compteur < 10001 :
    r = 1
    i=0
    while L[i] <=nbr**0.5 :
        r = r * nbr%L[i]
        i = i + 1
    if r !=0 : 
        L.append(nbr)
        compteur = compteur + 1
    nbr = nbr+1
print(L)
end=time.time()
print(f"temps pour trouver la réponse : {end-start}")
# temps pour trouver la réponse : 2.912987232208252