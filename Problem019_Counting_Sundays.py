# -*- coding: utf-8 -*-
# Problem 019 Counting Sundays
#You are given the following information, but you may prefer to do some 
#research for yourself.
#
#    - 1 Jan 1900 was a Monday.
#    - Thirty days has September,
#        April, June and November.
#        All the rest have thirty-one,
#        Saving February alone,
#        Which has twenty-eight, rain or shine.
#        And on leap years, twenty-nine.
#    - A leap year occurs on any year evenly divisible by 4, but not on a 
#    century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth 
#century (1 Jan 1901 to 31 Dec 2000)?
import time
start=time.time()
###########################
jour=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet",    
    "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]
longueur=[31,28,31,30,31,30,31,31,30,31,30,31]
longueur_leap=[31,29,31,30,31,30,31,31,30,31,30,31]

u=365%7
compteur=0
for i in range(1,101) :
    for j in range(12) :
        if i%4!=0 and i!=100: 
            u=(u+longueur[j])%7 
        else : 
            u=(u+longueur_leap[j])%7
        if u==6 :
            compteur=compteur+1
            print(f"le 1er {mois[j]} {1900+i} était un {jour[u]}")
print(compteur)
##########################
#temps pour trouver la réponse : 
end=time.time()
print(f"temps pour trouver la réponse : {end-start}") 

