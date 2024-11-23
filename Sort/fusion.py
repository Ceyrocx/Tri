# from visualisation import visualisation
from random import shuffle


L = [i for i in range(1, 101)]  # Creates a list containing integers from 1 to `amount` (inclusive).
shuffle(L)  # Randomly shuffles the elements of the list `L` to disorder them.

print(f"final : {partage(L, 0)}")
