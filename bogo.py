from random import shuffle
from math import ceil, factorial
from visualisationTri import visualisation

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

		visualisation(L, passage, titre="Bogo", nbTest=y)

		# if passage:
		# 		return L, y

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
			
		
