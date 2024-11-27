import matplotlib.pyplot as plt
import numpy as np

def visualisation(L, time=0.01, titre=None, nbTest=None):
    """
    Visualize the state of a list `L` as a bar chart, updating the heights of the bars
    based on the current values in the list. The visualization dynamically updates with each call.

    Parameters:
        L (list): The list of numerical elements to visualize.
        verif (bool): Flag to indicate if this is the final visualization (highlights bars in red).
        time (float, optional): Delay (in seconds) between updates. Default is 0.01 seconds.
        titre (str, optional): Title for the visualization. Default is None.
        nbTest (int, optional): The test iteration number, displayed on the plot. Default is None.

    Returns:
        None: This function directly updates the plot.
    """
    n = len(L)  # Length of the input list
    x = np.arange(1, n + 1, 1)  # Generate x-axis positions for the bars
    # Initialize the plot on the first call
    if not hasattr(visualisation, "initialized"):
        visualisation.LTrier = sorted(L)
        # Store bar references for future updates
        visualisation.bars = []

        # Create the initial figure and configure its settings
        plt.figure(figsize=(8, 6))
        plt.title(titre, color="orange", loc="center", fontweight="bold")

        # Create the bar chart and store the bars for later updates
        visualisation.bars.extend(plt.bar(x, L, color="orange"))
        plt.draw()  # Draw the initial state
        visualisation.initialized = True  # Mark initialization complete

    # Update the test number if provided
    if nbTest is not None:
        # Remove previous test number text if it exists
        for txt in plt.gca().texts:
            txt.remove()
        # Add the current test number
        plt.text(
            0.98, 1.02, f"Test n°{nbTest}", ha="right", fontsize=10, transform=plt.gca().transAxes
        )

    # Update bar heights and colors dynamically
    for bar, height in zip(visualisation.bars, L):
        bar.set_height(height)  # Update the bar height
        if L == visualisation.LTrier:
            bar.set_color("red")  # Highlight the bars in red if final visualization

    plt.pause(time)  # Pause to render the updates

    # Show the plot when final verification is requested
    if L == visualisation.LTrier:
        plt.show()
