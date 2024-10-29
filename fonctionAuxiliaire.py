from math import ceil, factorial
import numpy as np
import matplotlib.pyplot as plt


def verif(x, tri):
	"""
    Vérifie si une liste est triée après application d'un algorithme de tri.

    Args:
        x (list): La liste d'origine à trier.
        tri (function): La fonction de tri à appliquer à la liste.

    Returns:
        bool: True si la liste est triée, False sinon.
    """
	# Applique l'algorithme de tri à la liste d'entrée x
	L = tri(x)

	# Parcourt la liste triée pour vérifier l'ordre
	for i in range(1, len(L)):
		# Si un élément est plus grand que l'élément suivant, la liste n'est pas triée
		if L[i - 1] > L[i]:
			return False

	# Si aucun élément ne viole l'ordre, la liste est triée
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

