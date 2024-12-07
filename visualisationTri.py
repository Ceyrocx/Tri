import matplotlib.pyplot as plt
import numpy as np
import winsound
from math import log

def visualisation(L, time, sound, titre=None, nbTest=None):
    """
    Visualize the state of a list `L` as a bar chart, updating the heights of the bars
    based on the current values in the list. The visualization dynamically updates with each call.

    Parameters:
        L (list): The list of numerical elements to visualize.
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
        visualisation.LTrier = sorted(L)  # Store the sorted version of the list for later checks
        visualisation.bars = []  # Initialize a list to store bar references for updates
        visualisation.ancienL = L  # Track the previous state of the list
        visualisation.i= 0
        visualisation.verif = True

        # Create the initial figure and configure its settings
        plt.figure(figsize=(8, 6))
        plt.title(titre, color="orange", loc="center", fontweight="bold")

        # Create the bar chart and store the bars for later updates
        visualisation.bars.extend(plt.bar(x, L, color="orange"))  # Initial bar chart
        plt.draw()  # Draw the initial state
        visualisation.initialized = True  # Mark initialization as complete

    # Update the test number if provided
    if nbTest is not None:
        # Remove previous test number text if it exists
        for txt in plt.gca().texts:
            txt.remove()  # Clear the old test number
        # Add the current test number
        plt.text(
            0.98, 1.02, f"Test n°{nbTest}", ha="right", fontsize=10, transform=plt.gca().transAxes
        )

    # Update bar heights and colors dynamically
    i = 0

    if visualisation.i == 0:
        for bar, height in zip(visualisation.bars, L):
            bar.set_color("orange")  # Set the default color of the bars to orange
            bar.set_height(height)  # Update the height of each bar

            if height != visualisation.ancienL[i]:  # If the bar height has changed
                if sound is True:
                    winsound.Beep(round(2000*log(height)+2000), 50)
                bar.set_color("green")  # Highlight it in green
                visualisation.dernier = bar

            i += 1

    # Store the current list state to track changes in the next iteration
    visualisation.ancienL = L[:]

    # Pause to render the updated plot with the specified delay
    plt.pause(time)

    # Show the plot when the list is fully sorted (final verification)
    if L == visualisation.LTrier:

        if visualisation.i == 0:
            for bar in visualisation.bars:
                bar.set_color("orange")  # Change the color of the bars to red for the final visualization
            plt.pause(1)

        while visualisation.i < len(L):
            visualisation.bars[visualisation.i].set_color("green")
            if sound:
                winsound.Beep(round(2000 * log(L[visualisation.i]) + 2000), 50)
            visualisation.i += 1
            visualisation(L, time, sound, titre=titre, nbTest=nbTest)

        finish = True

        if finish == True and visualisation.verif:
            visualisation.verif = False
            for bar in visualisation.bars:
                bar.set_color("red")  # Change the color of the bars to red for the final visualization


            if  visualisation.i == len(L) and sound:
                plt.pause(1)
                winsound.PlaySound('Sound/Rick_Roll.wav', winsound.SND_FILENAME)
                visualisation.i += 1

            plt.show()
