from bubble import bubble
from bogo import bogo

def verif(x, tri):
	L = tri(x)
	for i in range(1, len(L)):
		if L[i-1] > L[i]:
			return False
	return True