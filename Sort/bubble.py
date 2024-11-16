from visualisationTri import visualisation

def bubble(L, time):
    """
    Sorts a list using the bubble sort algorithm and visualizes each step of the sorting process.

    Parameters:
    L (list): The list of elements to be sorted.
    time (float): The time delay between visualizations, in seconds.

    This function repeatedly steps through the list, compares adjacent elements, and swaps them
    if they are in the wrong order. The pass through the list is repeated until the list is sorted.
    """
    n = len(L)  # Get the length of the list L

    # Outer loop for each pass through the list
    for j in range(n, 0, -1):
        # Inner loop for comparing adjacent elements
        for i in range(1, j):
            # Compare the current element with the previous one
            if L[i] < L[i-1]:
                # Swap elements if they are in the wrong order
                L[i], L[i-1] = L[i-1], L[i]  # Swap the largest element to the end
            # Visualize the current state of the list after each comparison
            visualisation(L, verif=False, titre="Bubble Sort", time=time)

    # Final visualization when sorting is complete
    visualisation(L, verif=True, titre="Bubble sort", time=time)

    # return L  # Optionally return the sorted list
