# -*- coding: utf-8 -*-
# Problem 017 Number letter counts
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
#then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
#
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
#forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 
#20 letters. The use of "and" when writing out numbers is in compliance 
#with British usage.
import time
start=time.time()
###########################
noms=["one","two","three","four","five","six","seven","eight","nine","ten", 
      "eleven", "twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty", ""]
dizaines = ["twenty", "thirty","forty","fifty","sixty","seventy","eighty","ninety"]
centaines=["hundred", "thousand"]

def compteur(nbr) :
    j = nbr//100
    i = nbr%100
    reponse = 0
    if j > 0 :
        reponse = reponse + len(noms[j-1]) + len(centaines[0])  
    if i > 0 and j > 0:
        reponse = reponse + len("and")
    if i//10 >= 2:
        reponse = reponse + len(dizaines[(i//10)%10 -2])+ len(noms[i%10-1])
    elif i//10 == 1 :
        reponse = reponse + len(noms[i%10+9])  
    elif i//10 == 0 :
        reponse = reponse + len(noms[i%10-1])
    return reponse
    
somme=0
for k in range(1,1000) :
    somme = somme + compteur(k)
somme = somme + len(centaines[1]) + len(noms[0])
print(somme)
##########################
#temps pour trouver la réponse : 
end=time.time()
print(f"temps pour trouver la réponse : {end-start}") 