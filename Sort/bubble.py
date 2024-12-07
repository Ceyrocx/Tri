from visualisationTri import visualisation

def bubble(L, time, sound):
    """
    Sorts a list using the bubble sort algorithm and visualizes each step of the sorting process.

    Parameters:
    L (list): The list of elements to be sorted.
    time (float): The time delay between visualizations, in seconds.

    This function repeatedly steps through the list, compares adjacent elements, and swaps them
    if they are in the wrong order. The pass through the list is repeated until the list is sorted.
    """

    j = len(L)  # Get the length of the list L
    trier = False

    # Outer loop for each pass through the list
    while j >= 1 and trier is False:
        trier = True
        # Inner loop for comparing adjacent elements
        for i in range(1, j):
            # Compare the current element with the previous one
            if L[i] < L[i-1]:
                # Swap elements if they are in the wrong order
                L[i], L[i-1] = L[i-1], L[i]  # Swap the largest element to the end
                trier = False
            # Visualize the current state of the list after each comparison
            visualisation(L, sound=sound, titre="Bubble Sort", time=time)
        j -= 1

    # return L  # Optionally return the sorted list (commented out)
