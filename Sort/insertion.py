from visualisationTri import visualisation

def insertion(L):
    """
    Sorts a list using the Insertion Sort algorithm and visualizes each step of the sorting process.

    Parameters:
    L (list): The list of elements to be sorted.

    Returns:
    None: The function visualizes the sorting process and sorts the list in place.
    """

    # Loop through each element of the list
    for i in range(1, len(L)):
        j = i
        # Move the current element to its correct position in the sorted portion of the list
        while j > 0 and L[j - 1] > L[j]:
            # Swap adjacent elements if they are in the wrong order
            L[j - 1], L[j] = L[j], L[j - 1]
            # Visualize the list after each swap
            visualisation(L, titre="Insertion Sort")
            j -= 1

    # Final visualization of the sorted list
    visualisation(L, titre="Insertion Sort")
