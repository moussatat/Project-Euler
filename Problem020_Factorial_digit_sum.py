# -*- coding: utf-8 -*-
# Problem 020 Factorial digit sum
#n! means n × (n − 1) × ... × 3 × 2 × 1
#
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
#Find the sum of the digits in the number 100!
import time
start=time.time()
###########################
import math
mot=str(math.factorial(100))
somme = 0
for i in mot :
    somme = somme + int(i)
print(somme)
 
##########################
#temps pour trouver la réponse : 
end=time.time()
print(f"temps pour trouver la réponse : {end-start}") 
