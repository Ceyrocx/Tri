from visualisationTri import visualisation

def frequency(L, time, sound):
    """
    Sorts a list using the Frequency Sort algorithm and visualizes each step of the sorting process.

    Parameters:
    L (list): The list of positive integers to be sorted.
    time (float): The delay (in seconds) between each visualization step.
    sound (bool): Whether to play a sound during visualization.

    Returns:
    None: The list `L` is sorted in place, and the sorting process is visualized.
    """

    # Initialize a list to count the frequency of each value in `L`
    LTrier = [0] * max(L)  # Frequency list with size equal to the maximum value in L

    # Count the occurrences of each value in the list
    for value in L:
        LTrier[value - 1] += 1  # Increment the position corresponding to the value

    # Visualize the initial state of the list
    visualisation(L, sound=sound, titre="Frequency Sort", time=time)

    # Reconstruct the list `L` based on the counted frequencies
    index = 0  # Index to track the position in the original list
    for i in range(len(LTrier)):
        # Place the value `i+1` in the list according to its frequency
        for _ in range(LTrier[i]):  # Repeat based on frequency count
            L[index] = i + 1  # Set the value in the original list
            index += 1  # Move to the next position
            # Visualize the current state of the list after each insertion
            visualisation(L, sound=sound, titre="Frequency Sort", time=time)
