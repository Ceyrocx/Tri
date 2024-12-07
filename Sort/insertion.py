from visualisationTri import visualisation

def insertion(L, time, sound):
    for i in range(len(L)):
        j = i
        while j > 0 and L[j-1] > L[j]:
            L[j-1], L[j] = L[j], L[j-1]
            visualisation(L, sound=sound, titre="Insertion Sort", time=time)
            j -= 1

    visualisation(L, sound=sound, titre="Selection Sort", time=time)
