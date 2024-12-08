from visualisationTri import visualisation
from random import shuffle

def bogo(L):
    """
    Sort a list using the Bogo sort algorithm, which repeatedly shuffles the list
    until it is sorted. The process is visualized after each shuffle.

    Parameters:
    L (list): The list of elements to be sorted.

    Returns:
    None: This function does not return a value but visualizes the sorting process.
    """

    LTrier = sorted(L)  # Create a sorted version of the list for comparison
    counter = 0  # Counter for the number of shuffle attempts

    # Continue shuffling until the list is sorted
    while L != LTrier:
        counter += 1  # Increment shuffle attempt counter
        shuffle(L)  # Shuffle the list randomly

        # Visualize the current state of the list after shuffling
        visualisation(L, titre="Bogo Sort", nbTest=counter)

    # Once sorted, visualization confirms the final sorted list
