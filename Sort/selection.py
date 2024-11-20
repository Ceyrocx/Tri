from visualisationTri import visualisation

def selection(L, time):
    n = len(L)
    for i in range(n):
        min = L[i]
        indMin = i
        for j in range(i+1, n):
            if L[j]<min:
                min = L[j]
                indMin = j
        L[i], L[indMin] = L[indMin], L[i]
        visualisation(L, verif=False, titre="Selection Sort", time=time)

    visualisation(L, verif=True, titre="Selection Sort", time=time)