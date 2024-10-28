from random import *
from math import *
from visualisationTri import *

amount = 9
L = []
while True:
	i = randint(0, amount-1)
	if i not in L:
		L.append(i)
	if len(L) == amount:
		break

def bogo(L):
	y = 0
	
	while True:
		passage = True
		y += 1
		print("test", y)
		shuffle(L)

		for i in range(1, len(L)):
			if L[i-1] > L[i]:
				passage = False
				break

		visualisation(L, passage, legende="Bogo", nbTest=y)

		if passage:
				return L, y

bogo(L)

def moyenne(x, z, seuil):
	i = 0
	y = 0
	while i < seuil:
		y += bogo(x)[1]
		i += 1
		if i%100 == 0:
			print(i)
	moyenne = y // seuil
	return ceil(moyenne), y/seuil, ceil(moyenne) == factorial(z)
				
# print(moyenne(x, z, 10000))
			
		
