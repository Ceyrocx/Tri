import matplotlib.pyplot as plt
import numpy as np

def visualisation(L, verif, time=0.01, titre=None, nbTest=None):
    """
    Visualizes the state of a list L as a bar chart, updating the heights of the bars
    based on the values in the list. The visualization is updated at each call.

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

    # Check if this is the first call to initialize the plot
    if not hasattr(visualisation, "initialized"):
        visualisation.bars = []
        plt.figure()  # Create a new figure for plotting

        # Set up the title and text on the first call
        plt.title(titre, color="orange", loc="center", fontweight="bold")

        # Initialize the bars on the first call
        visualisation.bars.clear()  # Clear any existing bars
        visualisation.bars.extend(plt.bar(x, L, color="orange"))  # Create the initial bar plot
        plt.draw()  # Draw the initial figure
        visualisation.initialized = True  # Set flag to indicate initialization complete

    # Display the test number if provided
    if nbTest is not None:
        for txt in plt.gca().texts:
            txt.remove()
        plt.text(0.98, 1.02, f"Test n°{nbTest}", ha="right", fontsize=10, transform=plt.gca().transAxes)

    # Update bar heights for each call
    for bar, height in zip(visualisation.bars, L):
        bar.set_height(height)  # Update each bar's height with the current value

    plt.pause(time)  # Allow the plot to update with the new heights

    # If verification is requested, show the final plot
    if verif:
        plt.show()  # Display the final plot
