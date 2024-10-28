from random import *
from math import *
from visualisationTri import *

amount = 101
L = []
while True:
	i = randint(0, 100)
	if i not in L:
		L.append(i)
	if len(L) == amount:
		break


def verif(x):
	L = bubble(x)
	for i in range(1, len(L)):
		if L[i-1] > L[i]:
			return False
	return True
		
def bubble(L):
	verif = False
	for j in range(len(L), 0, -1):
		max = L[0]
		ind = 0
		
		for i in range(j):
			if max < L[i]:
				max = L[i]
				ind = i
		L[ind], L[j-1] = L[j-1], L[ind]
		if j == 1:
			verif = True
		visualisation(L, verif, legende="Bubble")
		
	return L	

print(verif(L))		