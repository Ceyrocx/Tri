from math import ceil, factorial
import numpy as np
import matplotlib.pyplot as plt


def verif(x, tri):
    """
    Verifies if a list is sorted after applying a sorting algorithm.

    Args:
        x (list): The original list to be sorted.
        tri (function): The sorting function to be applied to the list.

    Returns:
        bool: True if the list is sorted, False otherwise.
    """
    # Apply the sorting algorithm to the input list x
    L = tri(x)

    # Iterate through the sorted list to check the order
    for i in range(1, len(L)):
        # If an element is greater than the next one, the list is not sorted
        if L[i - 1] > L[i]:
            return False

    # If no element violates the order, the list is sorted
    return True


def visualisation2(L, bars, verif, time=0.01, titre=None, nbTest=None):
    """
    A secondary visualization function that creates a bar chart of a list L.
    This version clears the plot for each update.

    Parameters:
    L (list): The list of elements to visualize.
    bars (list): A list to hold the bar objects for updating their heights.
    verif (bool): Flag to indicate whether to show the final plot.
    time (float, optional): Time delay for the pause between updates. Default is 0.01 seconds.
    titre (str, optional): Title for the plot. Default is None.
    nbTest (int, optional): Test number to display on the plot. Default is None.

    Returns:
    None: This function does not return a value; it updates the plot in place.
    """
    n = len(L)  # Get the length of the list L
    x = np.arange(1, n + 1, 1)  # Create an array for x-axis values

    plt.pause(time)  # Pause for the specified time to allow for updates
    plt.clf()  # Clear the current figure

    plt.subplots_adjust(top=0.85)  # Adjust the subplot parameters
    plt.title(titre, color="orange", loc="center", fontweight="bold")  # Set the plot title

    # Display the test number if provided
    plt.text(x=1, y=1.022, s=f"Test n°{nbTest}", ha="right", fontsize=10, transform=plt.gca().transAxes)

    # Create the bar plot with updated values
    plt.bar(x, L, color="orange")  # Create a new bar plot with current values

    # If verification is requested, show the final plot
    if verif:
        plt.show()  # Display the final plot

# amount = 150
# L = np.random.randint(0, 100, amount)
# x = np.arange(0, amount, 1)


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


def fusion(Lpetit, Lgrand, time):
    """
    Merges two sorted lists, `Lpetit` and `Lgrand`, into a single sorted list,
    visualizing the result after each merge step.

    Args:
        Lpetit (list): The list of smaller elements.
        Lgrand (list): The list of larger elements.
        time (float): The delay (in seconds) between each visualization.

    Returns:
        list: A merged list containing elements from both `Lpetit` and `Lgrand`, sorted.
    """

    result = []  # List to store the merged result

    # Add elements from Lpetit to result
    if len(Lpetit) > 0:
        for val in Lpetit:
            result.append(val)

    # Add elements from Lgrand to result
    if len(Lgrand) > 0:
        for val in Lgrand:
            result.append(val)

    # Visualize the current state of the merged list
    visualisation(result, verif=False, titre="Quick Sort", time=time)
    print(result)  # Print the merged list (optional for debugging)
    return result  # Return the merged list


def quick(LTri, a, b, time):
    """
    Implements the Quick Sort algorithm with recursive partitioning and visualization at each step.

    Args:
        LTri (list): The list of elements to be sorted.
        a (int): The start index of the current sublist to be sorted.
        b (int): The end index of the current sublist to be sorted.
        time (float): The delay (in seconds) between each visualization.

    Returns:
        list: The sorted list.
    """

    # Base case: if the sublist size is less than 1, return the list as it's already sorted
    if b - a < 1:
        return LTri

    # Choose the pivot as the last element in the current sublist
    pivot = LTri[b-a-1]
    Lpetit = []  # List to store elements smaller than the pivot
    Lgrand = []  # List to store elements greater than the pivot

    # Partition the list into smaller and larger elements
    for element in LTri:
        if element < pivot:
            Lpetit.append(element)  # Append smaller elements
        elif element > pivot:
            Lgrand.append(element)  # Append larger elements

    Lpetit.append(pivot)  # Add the pivot to the list of smaller elements

    # Determine the new position of the pivot after partitioning
    posPivot = len(Lpetit) - 1
    b = posPivot + len(Lgrand)

    # Visualize the current state of the list
    visualisation(LTri, verif=False, titre="Quick Sort", time=time)

    # Recursively sort the left and right sublists and merge them
    return fusion(quick(Lpetit, a, posPivot, time), quick(Lgrand, posPivot + 1, b, time), time)