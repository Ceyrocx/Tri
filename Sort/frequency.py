from visualisationTri import visualisation

def frequency(L, time):
    """
    Implements the Frequency Sort algorithm with visualization.

    Args:
        L (list): The list of positive integers to sort.
        time (float): The delay (in seconds) between each visualization step.

    Returns:
        None: The list `L` is sorted in place.
    """

    # Initialize a list to count the frequency of each value
    LTrier = [0] * max(L)  # Size is based on the maximum value in `L`

    # Count the occurrences of each value in the list
    for value in L:
        LTrier[value - 1] += 1  # Increment the position corresponding to the value

    # Reconstruct the list `L` based on the counted frequencies
    for i in range(len(LTrier)):
        for j in range(i, i + LTrier[i]):  # For each occurrence of the value `i + 1`
            L[j] = i + 1  # Place the value in the sorted list
            # Visualize the current state of the list after each insertion
            visualisation(L, verif=False, titre="Frequency Sort", time=time)

    # Final visualization once the sorting is complete
    visualisation(L, verif=True, titre="Frequency Sort", time=time)
