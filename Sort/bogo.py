from random import shuffle
from visualisationTri import visualisation

def bogo(L, time, sound):
    """
    Sorts a list using the Bogo sort algorithm, which repeatedly shuffles the list
    until it is sorted, and visualizes each shuffle attempt.

    Parameters:
    L (list): The list of elements to be sorted.
    time (float): The time delay between visualizations, in seconds.

    Returns:
    None: This function does not return a value; it visualizes the sorting process.
    """

    LTrier = sorted(L)  # Create a sorted copy for verification
    passage = False  # Flag to check if the list is sorted
    counter = 0  # Counter for the number of shuffles

    while True:
        counter += 1  # Increment the shuffle count
        # print("test", y)  # Print the current shuffle attempt number
        shuffle(L)  # Shuffle the list randomly

        # Check if the list is sorted
        if L == LTrier:
            passage = True

        # Visualize the current state of the list after shuffling
        visualisation(L, sound=sound, titre="Bogo Sort", time=time, nbTest=counter)

        # Optionally return the sorted list and the number of attempts
        if passage:
            break
        #     return L, y
