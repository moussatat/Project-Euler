# -*- coding: utf-8 -*-
# Problem 003 Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# No need to check for prime, we are getting smalled factor that is different from 1. and that is always a prime number.
import time
start = time.time()

liste=[]
nbr = 600851475143
d = 2
while nbr != 1 :
	if nbr%d==0 :
		liste.append(d)
		nbr=nbr//d
	else :
		d = d + 1
print(liste[-1])

end=time.time() 
print(L)
print(f"temps pour trouver la réponse : {end-start}")
