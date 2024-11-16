from visualisationTri import visualisation

def frequency(L, time):

    LTrier = [0] * max(L)

    for value in L:
        LTrier[value-1] += 1

    for i in range(len(LTrier)):
        for j in range(i, i + LTrier[i]):
            L[j] = i
            visualisation(L, verif=False, titre="Frequency Sort", time=time)

    visualisation(L, verif=True, titre="Frequency Sort", time=time)