# -*- coding: utf-8 -*-
# Problem 014 Longest Collatz sequence 
#The following iterative sequence is defined for the set of positive integers:
#
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#
#Using the rule above and starting with 13, we generate the following sequence:
#
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?
#
#NOTE: Once the chain starts the terms are allowed to go above one million.
import time
start=time.time()
###########################
# Method 1
n=10**6

D = [ -1 for i in range(0,n+1)]
for i in range(1,n+1) :
    u = i
    D[i]=0
    compteur = 0
    while u > 1 :
        if u%2==0 :
            u = u//2
            compteur = compteur + 1
        else :
            u = (3 * u + 1)//2
            compteur = compteur + 2
            ## if n is odd, the next term is even, gain 1/2 a second
        if u <= n and D[u] != -1 :
            break
    D[i] = D[u] + compteur 

maximum = max(D)
rang=D.index(max(D))
print(rang, maximum)
##########################
#temps pour trouver la réponse : 
end=time.time()
print(f"temps pour trouver la réponse : {end-start}") 
start=time.time()
##########################
# Method 2
#n=10**6  
D = [ -1 for i in range(0,n+1)]
D[1]=0
j = 1
while j <=  n :
    i = j
    while D[i] != -1 and i<n :
        i = i + 1
    j = i + 1 
    L = [i]
    u = i
    compteur = 0
    while u > 1 :
        if u%2==0 :
            u = u//2
            compteur = compteur + 1
        else :
            u = (3 * u + 1)//1
            compteur = compteur + 1
        if  u <= n and D[u] != -1 :
            break 
        L.append(u)
    for k in range(len(L)) :
        if L[k] <= n :
            D[L[k]] = D[u] + compteur - k
#    j = j + 1

maximum = max(D)
rang=D.index(max(D))
print(rang, maximum)
##########################
#temps pour trouver la réponse : 
end=time.time()
print(f"temps pour trouver la réponse : {end-start}") 
start=time.time()
##########################
# Given answer on site
def collatz(n) :
    if n == 1 :
        return 0
    elif n%2==0 :
        return 1 + collatz(n//2)
    else :
        return 2 + collatz((3*n+1)//2)
 
reponse=0
maximum= -1
for i in range(n//2, n+1) :
    longueur=collatz(i)
    if maximum < longueur:
        reponse=i
        maximum = longueur
print(reponse, maximum)
##########################
#temps pour trouver la réponse : 
end=time.time()
print(f"temps pour trouver la réponse : {end-start}") 
 