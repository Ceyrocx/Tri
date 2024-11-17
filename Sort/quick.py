from visualisationTri import visualisation

def quick(L, time, a=None, b=None):
    """
    Implémente l'algorithme de tri rapide (Quick Sort) avec visualisation à chaque étape.

    Args:
        L (list): La liste d'éléments à trier.
        time (float): Le délai (en secondes) entre chaque étape de visualisation.
        a (int, optional): L'index de début de la sous-liste à trier. Par défaut None.
        b (int, optional): L'index de fin de la sous-liste à trier. Par défaut None.

    Returns:
        list: La liste triée L.
    """

    # Initialisation des paramètres au premier appel
    if not hasattr(quick, "initialised"):
        a = 0  # Index de début de la liste
        b = len(L)  # Index de fin de la liste
        quick.LTrier = sorted(L)  # Créer une copie triée pour vérifier la fin du tri
        quick.initialised = True  # Marquer l'initialisation comme complète

    # Condition d'arrêt de la récursivité: la sous-liste est de taille inférieure à 2
    if b - a < 2:
        return L

    # Choisir le dernier élément comme pivot
    pivot = L[b - 1]
    Lpetit = []  # Liste pour les éléments plus petits que le pivot
    Lgrand = []  # Liste pour les éléments plus grands que le pivot

    # Partitionner les éléments autour du pivot
    for i in range(a, b - 1):  # Parcourir les éléments sauf le pivot
        if L[i] < pivot:
            Lpetit.append(L[i])
        else:
            Lgrand.append(L[i])

    # Reconstruire la liste en plaçant les éléments plus petits, le pivot, et les plus grands
    L[a:a + len(Lpetit)] = Lpetit  # Placer les éléments plus petits
    L[a + len(Lpetit)] = pivot  # Placer le pivot à sa position correcte
    L[a + len(Lpetit) + 1:b] = Lgrand  # Placer les éléments plus grands

    posPivot = a + len(Lpetit)  # Nouvelle position du pivot

    # Visualiser l'état actuel de la liste après partition
    visualisation(L, verif=False, titre="Quick Sort", time=time)

    # Appel récursif pour trier la partie gauche (éléments plus petits que le pivot)
    quick(L, time, a=a, b=posPivot)

    # Appel récursif pour trier la partie droite (éléments plus grands que le pivot)
    quick(L, time, a=posPivot + 1, b=b)

    # Si la liste est complètement triée, effectuer la visualisation finale
    if L == quick.LTrier:
        visualisation(L, verif=True, titre="Quick Sort", time=time)
