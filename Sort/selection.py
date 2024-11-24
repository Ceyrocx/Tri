from visualisationTri import visualisation

def selection(L, time):
    """
    Sorts a list using the selection sort algorithm and visualizes each step of the sorting process.

    Parameters:
    L (list): The list of elements to be sorted.
    time (float): The time delay between visualizations, in seconds.

    The selection sort algorithm repeatedly selects the smallest element from the unsorted portion
    of the list and swaps it with the first unsorted element. This process is repeated until the list is sorted.
    """

    n = len(L)  # Get the length of the list L

    # Loop over each element in the list
    for i in range(n):
        min = L[i]  # Set the current element as the minimum
        indMin = i  # Index of the minimum element

        # Find the smallest element in the unsorted portion of the list
        for j in range(i + 1, n):
            if L[j] < min:
                min = L[j]
                indMin = j

        # Swap the found minimum element with the current element
        L[i], L[indMin] = L[indMin], L[i]

        # Visualize the current state of the list after each swap
        visualisation(L, titre="Selection Sort", time=time)

