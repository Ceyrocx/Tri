import argparse
from random import shuffle

from Sort.bogo import bogo
from Sort.bubble import bubble
from Sort.frequency import frequency
from Sort.quick import quick
from Sort.selection import selection
from Sort.fusion import merge

# Dictionary associating algorithm names with their respective functions
dictTri = {
    "bogo": bogo,    # Algorithme de tri Bogo
    "bubble": bubble,  # Algorithme de tri à bulles
    "frequency": frequency,
    "quick": quick,
    "selection": selection,
    "merge": merge,
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

    L = [i for i in range(1, amount + 1)]  # Creates a list containing integers from 1 to `amount` (inclusive).
    shuffle(L)  # Randomly shuffles the elements of the list `L` to disorder them.

    # Call the appropriate sorting function from the dictionary using the specified algorithm
    dictTri[tri.lower()](L, time)


if __name__ == "__main__":
    # Initialize the argument parser for command-line arguments
    parser = argparse.ArgumentParser(description="An example script with command-line arguments.")

    # Define the arguments
    parser.add_argument("-n", "--amount", type=int, default=5, help="Number of elements to sort")
    parser.add_argument("-t", "--tri", type=str, default="bogo", help="Sorting algorithm to use (bogo or bubble)")
    parser.add_argument("-s", "--speed", type=float, default=0.01, help="Speed of the sorting visualization")

    # Parse the arguments
    args = parser.parse_args()

    # Call the function with the obtained parameters
    run(amount=args.amount, tri=args.tri, time=args.speed)
