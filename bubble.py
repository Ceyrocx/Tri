from random import *
from math import *

z = 6000
x = [randint(-20000,20000) for i in range(z)]

def verif(x):
	L = bubble(x)
	for i in range(1, len(L)):
		if L[i-1] > L[i]:
			return False
	return True
		
def bubble(L):
	for j in range(len(L), 0, -1):
		max = L[0]
		ind = 0
		
		for i in range(j):
			if max < L[i]:
				max = L[i]
				ind = i
		L[ind], L[j-1] = L[j-1], L[ind]
		
	return L	

print(verif(x))		