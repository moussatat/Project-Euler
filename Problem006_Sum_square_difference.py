# -*- coding: utf-8 -*-
# Problem 006 Sum square difference
#The sum of the squares of the first ten natural numbers is,
#
#1**2 + 2**2 + ... + 10**2 = 385
#The square of the sum of the first ten natural numbers is,
#
#(1 + 2 + ... + 10)**2 = 55**2 = 3025
#Hence the difference between the sum of the squares of the first ten natural 
#numbers and the square of the sum is 3025 − 385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred 
#natural numbers and the square of the sum.

import time

start=time.time()
n =100
somme_des_carres=0
for i in range(n+1) :
    somme_des_carres=somme_des_carres + i**2
somme = 0
for i in range(n+1):
    somme = somme + i
    
print(somme**2-somme_des_carres)
end=time.time()
print(f"temps pour trouver la réponse : {end-start}")