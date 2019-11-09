# -*- coding: utf-8 -*-
#Problem 010 Summation of primes
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.
import time

start=time.time()
L = [2]
somme = 0
nbr= 2
while nbr < 2*10**6 :
    r = 1
    j=0
    while L[j]<=nbr**0.5 and j<len(L):
        r = r * nbr%L[j]
        j=j+1
#    for j in L : 
#        r = r * nbr%j 
    if r != 0 :     # nbr est premier
        L.append(nbr)
        somme = somme + nbr
    nbr = nbr+1
print(somme)
end=time.time()
print(f"temps pour trouver la réponse : {end-start}")
# Réponse : 142913828922
#temps pour trouver la réponse : 248.07689476013184