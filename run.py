import argparse
from random import randint

from bogo import bogo
from bubble import bubble


dictTri = {"bogo": bogo,
           "bubble": bubble,
           }

def run(amount, tri):
    L = []
    while True:
        i = randint(0, amount - 1)
        if i not in L:
            L.append(i)
        if len(L) == amount:
            break
    dictTri[tri.lower()](L)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Un exemple de script avec des arguments.")

    # Définir les arguments
    parser.add_argument("-n", "--amount", type=int, default=8, help="Nombre d'élément à trier")
    parser.add_argument("-t", "--tri", type=str, default="bogo", help="Tri à utiliser")

    # Analyser les arguments
    args = parser.parse_args()

    # Appeler la fonction avec les paramètres obtenus
    run(amount=args.amount, tri=args.tri)