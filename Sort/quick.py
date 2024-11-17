from Tri.visualisationTri import visualisation
from random import shuffle

def quick(L, a, b, time):
    if b - a < 2:
        return L

    # Choisir le dernier élément comme pivot
    pivot = L[b - 1]
    Lpetit = []
    Lgrand = []

    for i in range(a, b - 1):  # Parcourir les éléments sauf le pivot
        if L[i] < pivot:
            Lpetit.append(L[i])
        else:
            Lgrand.append(L[i])
    print(f"Lpetit: {Lpetit}, Lgrand: {Lgrand}, pivot: {pivot}")
    # Reconstruire la liste en fonction du pivot
    L[a:a + len(Lpetit)] = Lpetit
    L[a + len(Lpetit)] = pivot
    L[a + len(Lpetit) + 1:b] = Lgrand

    posPivot = a + len(Lpetit)  # Nouvelle position du pivot

    # Visualiser après chaque partition
    visualisation(L, verif=False, titre="Quick Sort", time=time)

    # Appels récursifs pour trier les sous-listes
    quick(L, a, posPivot, time)
    quick(L, posPivot + 1, b, time)

    return L




L = [i for i in range(10)]
shuffle(L)
print(L)

print(quick(L, 0, len(L), 1))
