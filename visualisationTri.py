import matplotlib.pyplot as plt
import numpy as np
import winsound
from math import log

def visualisation(L, time, sound, titre=None, nbTest=None):
    """
    Visualizes the state of a list `L` as a dynamic bar chart, updating the heights and colors
    of the bars based on the current values in the list. A beep sound can be played when a bar
    changes height. The function keeps updating until the list is sorted.

    Parameters:
        L (list): The list of numerical elements to visualize.
        time (float): Delay (in seconds) between updates.
        sound (bool): Whether or not to play a sound when a bar changes height.
        titre (str, optional): Title for the visualization. Default is None.
        nbTest (int, optional): The test iteration number, displayed on the plot. Default is None.

    Returns:
        None: This function directly updates and displays the plot.
    """

    n = len(L)  # Length of the list
    x = np.arange(1, n + 1)  # Generate x-axis positions for the bars

    # Initialize the plot on the first call
    if not hasattr(visualisation, "initialized"):
        visualisation.LTrier = sorted(L)  # Store the sorted version of the list for comparison
        visualisation.bars = []  # Initialize bar container
        visualisation.ancienL = L[:]  # Store the previous state of the list
        visualisation.verif = True  # Used to verify if the list is fully sorted

        # Setup plot figure
        plt.figure(figsize=(12, 8))
        plt.title(titre, color="orange", loc="center", fontweight="bold")

        # Create initial bar chart and store bar objects for later updating
        visualisation.bars.extend(plt.bar(x, L, color="orange"))
        plt.draw()  # Draw the initial state
        visualisation.initialized = True  # Mark initialization as done

    # Update test number if provided
    if nbTest is not None:
        # Clear previous test number from the plot
        for txt in plt.gca().texts:
            txt.remove()
            # Display the new test number
        plt.text(0.98, 1.02, f"Test n°{nbTest}", ha="right", fontsize=10, transform=plt.gca().transAxes)

    # Update bar heights and colors
    for i, (bar, height) in enumerate(zip(visualisation.bars, L)):
        if height != visualisation.ancienL[i]:  # Check if the height has changed
            if sound:
                # Calculate frequency for the beep sound to be in a more audible range
                # This formula ensures that the frequency remains within a range that is clear and distinct
                # We limit the frequency to be between 1000 Hz and 4000 Hz.
                frequency = max(1000, min(4000, 1500 * log(height + 1) + 1500))  # Avoid extremely low frequencies
                winsound.Beep(int(frequency), 50)  # Play sound if height changes
            bar.set_color("green")  # Highlight changed bars in green
        else:
            bar.set_color("orange")  # Reset color to orange for all bars
        bar.set_height(height)  # Update the height of the bar

    # Store current state of the list to detect future changes
    visualisation.ancienL = L[:]

    # Pause to render the updated plot with the given time delay
    plt.pause(time)

    # Check if the list is sorted and update visualization accordingly
    if L == visualisation.LTrier and visualisation.verif:
        visualisation.verif = False  # Avoid repeating the final sorted checks

        i = 0
        # Final color transition of bars to green one by one
        while i < len(L):
            visualisation.bars[i].set_color("green")  # Set color to green for the final sorted state
            if sound:
                # Play sound for each bar transitioning to green
                frequency = max(1000, min(4000, 1500 * log(L[i] + 1) + 1500))  # Ensure frequency remains audible
                winsound.Beep(int(frequency), 50)
            i += 1
            plt.pause(time)

        # Final step: Change all bars to red and play the final sound
        for bar in visualisation.bars:
            bar.set_color("red")  # Final color change to red, indicating sorting completion
        plt.pause(1)  # Short pause before playing final sound

        if sound:
            # Play a final celebratory sound (e.g., Rick Roll sound)
            winsound.PlaySound('Sound/Rick_Roll.wav', winsound.SND_FILENAME)

        # Display final state of the visualization
        plt.show()
