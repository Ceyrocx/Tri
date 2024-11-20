from random import shuffle
from visualisationTri import visualisation

def bogo(L, time):
    """
    Sorts a list using the Bogo sort algorithm, which repeatedly shuffles the list
    until it is sorted, and visualizes each shuffle attempt.

    Parameters:
    L (list): The list of elements to be sorted.
    time (float): The time delay between visualizations, in seconds.

    Returns:
    None: This function does not return a value; it visualizes the sorting process.
    """

    counter = 0  # Counter for the number of shuffles

    while True:
        passage = True  # Flag to check if the list is sorted
        counter += 1  # Increment the shuffle count
        # print("test", y)  # Print the current shuffle attempt number
        shuffle(L)  # Shuffle the list randomly

        # Check if the list is sorted
        for i in range(1, len(L)):
            if L[i-1] > L[i]:  # If the previous element is greater than the current
                passage = False  # Set passage to False if the list is not sorted
                break  # Exit the loop early if unsorted

        # Visualize the current state of the list after shuffling
        visualisation(L, passage, titre="Bogo Sort", time=time, nbTest=counter)

        # Optionally return the sorted list and the number of attempts
        if passage:
            break
        #     return L, y
