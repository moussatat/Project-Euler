# -*- coding: utf-8 -*-
# Problem 016 Power digit sum
#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#What is the sum of the digits of the number 21000?
import time
start=time.time()
###########################
nbr=2**1000 
string = str(nbr)
reponse = 0
for i in string :
    reponse = reponse + int(i) 
print(reponse) 
##########################
#temps pour trouver la réponse : 
end=time.time()
print(f"temps pour trouver la réponse : {end-start}") 