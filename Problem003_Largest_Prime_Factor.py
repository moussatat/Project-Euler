# -*- coding: utf-8 -*-
# Problem 003 Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import time
  
def is_prime(nbr) :
    i = 2 
    while i <= nbr and nbr%i !=0:
        i = i + 1
    if i == nbr   :
        return True
    else :
        return False 
start = time.time()

n=600851475143
nbr = n 
L=[]
while nbr > 1 :
    i=2
    while i<=nbr and nbr%i != 0 : 
        i = i + 1 
    if nbr%i==0 :
        nbr = nbr//i 
        if is_prime(i) :
            L.append(i) 
end=time.time() 
print(L)
print(f"temps pour trouver la réponse : {end-start}")