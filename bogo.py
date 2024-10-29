from random import shuffle
from math import ceil, factorial
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
    y = 0  # Counter for the number of shuffles
    bars = []  # Initialize an empty list to store bar heights for visualization

    while True:
        passage = True  # Flag to check if the list is sorted
        y += 1  # Increment the shuffle count
        print("test", y)  # Print the current shuffle attempt number
        shuffle(L)  # Shuffle the list randomly

        # Check if the list is sorted
        for i in range(1, len(L)):
            if L[i-1] > L[i]:  # If the previous element is greater than the current
                passage = False  # Set passage to False if the list is not sorted
                break  # Exit the loop early if unsorted

        # Visualize the current state of the list after shuffling
        visualisation(L, bars, passage, titre="Bogo Sort", time=time, nbTest=y)

        # Optionally return the sorted list and the number of attempts
        # if passage:
        #     return L, y


def moyenne(x, z, seuil):
    """
    Computes the average number of shuffles required by the Bogo sort algorithm
    over a specified number of trials and checks if the average is equal to the
    factorial of a given number.

    Parameters:
    x (list): The list of elements to be sorted.
    z (int): The number to calculate the factorial for comparison.
    seuil (int): The number of trials to run.

    Returns:
    tuple: A tuple containing the average number of shuffles (rounded up),
           the average number of shuffles (as a float),
           and a boolean indicating whether the average equals the factorial of z.
    """
    i = 0  # Counter for the number of trials
    y = 0  # Sum of shuffles required over trials

    while i < seuil:
        # Execute Bogo sort and accumulate the number of attempts
        y += bogo(x)[1]  # Add the number of attempts from each trial
        i += 1  # Increment trial counter
        if i % 100 == 0:  # Print progress every 100 trials
            print(i)

    moyenne = y // seuil  # Calculate the average number of shuffles (integer division)
    # Return a tuple with the rounded average, the float average, and a comparison with factorial
    return ceil(moyenne), y / seuil, ceil(moyenne) == factorial(z)

# print(moyenne(x, z, 10000))  # Uncomment to run the average computation
			
		
