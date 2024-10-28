from visualisationTri import *

def bubble(L):
	passage = False
	for j in range(len(L), 0, -1):
		max = L[0]
		ind = 0
		
		for i in range(j):
			if max < L[i]:
				max = L[i]
				ind = i
		L[ind], L[j-1] = L[j-1], L[ind]

		if j == 1:
			passage = True
		visualisation(L, passage, titre="Bubble")

	# return L