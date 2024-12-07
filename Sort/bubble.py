from visualisationTri import visualisation

def bubble(L, time, sound):
    """
    Sorts a list using the bubble sort algorithm and visualizes each step of the sorting process.

    Parameters:
    L (list): The list of elements to be sorted.
    time (float): The time delay between visualizations, in seconds.
    sound (bool): Whether to play a sound during visualization.

    Returns:
    None: The function visualizes the sorting process without returning a value.
    """

    n = len(L)  # Get the length of the list L
    sorted_flag = False  # Flag to track if the list is sorted

    # Continue sorting until the list is fully sorted
    while not sorted_flag:
        sorted_flag = True  # Assume the list is sorted
        # Traverse the list up to the last unsorted element
        for i in range(1, n):
            # Compare adjacent elements and swap if in wrong order
            if L[i] < L[i - 1]:
                L[i], L[i - 1] = L[i - 1], L[i]  # Swap the two elements
                sorted_flag = False  # If a swap occurs, the list is not yet sorted

                # Visualize the list after each swap
                visualisation(L, sound=sound, titre="Bubble Sort", time=time)
        # Decrease n to avoid re-checking the last sorted element
        n -= 1
