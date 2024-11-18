import argparse
from random import shuffle

from Sort.bogo import bogo
from Sort.bubble import bubble
from Sort.frequency import frequency
from Sort.quick import quick

# Dictionnaire associant les noms d'algorithmes à leurs fonctions
dictTri = {
    "bogo": bogo,    # Algorithme de tri Bogo
    "bubble": bubble,  # Algorithme de tri à bulles
    "frequency": frequency,
    "quick": quick
}

def run(amount, tri, time):
    """
    Generates a unique list of random integers and applies the specified sorting algorithm on it.

    Parameters:
    amount (int): The number of unique elements to generate and sort.
    tri (str): The name of the sorting algorithm to use (either 'bogo' or 'bubble').
    time (float): The delay time between visualizations during sorting.

    Returns:
    None: This function does not return a value; it calls the sorting function.
    """
    L = [i for i in range(1, amount+1)]
    shuffle(L)

    # Call the appropriate sorting function from the dictionary using the specified algorithm
    dictTri[tri.lower()](L, time)


if __name__ == "__main__":
    # Initialize the argument parser for command-line arguments
    parser = argparse.ArgumentParser(description="Un exemple de script avec des arguments.")

    # Définir les arguments
    parser.add_argument("-n", "--amount", type=int, default=5, help="Nombre d'élément à trier")
    parser.add_argument("-t", "--tri", type=str, default="bogo", help="Tri à utiliser (bogo ou bubble)")
    parser.add_argument("-s", "--speed", type=float, default=0.01, help="Vitesse du Tri")

    # Analyser les arguments
    args = parser.parse_args()

    # Appeler la fonction avec les paramètres obtenus
    run(amount=args.amount, tri=args.tri, time=args.speed)
