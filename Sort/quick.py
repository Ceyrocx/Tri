from visualisationTri import visualisation

def quick(L, a=None, b=None):
    """
    Sorts the list `L` using the Quick Sort algorithm with visualizations.

    Args:
        L (list): The list of elements to sort.
        a (int, optional): The starting index of the sublist to sort. Defaults to 0.
        b (int, optional): The ending index of the sublist to sort. Defaults to the length of `L`.

    Returns:
        list: The sorted list `L`.
    """

    # Initialize the starting and ending indices on the first call
    if a is None and b is None:
        a = 0  # Start of the list
        b = len(L)  # End of the list
        visualisation(L, titre="Quick Sort")

    # Base case: Stop recursion if the sublist has fewer than 2 elements
    if b - a < 2:
        return L

    # Choose the last element as the pivot
    pivot = L[b - 1]

    # Partition: Rearrange elements around the pivot
    left, right = a, b - 1  # Indices for partitioning
    while left < right:
        # Move left pointer to find an element larger than the pivot
        while left < right and L[left] < pivot:
            left += 1
        # Move right pointer to find an element smaller than the pivot
        while left < right and L[right] >= pivot:
            right -= 1
        # Swap elements if necessary
        if left < right:
            L[left], L[right] = L[right], L[left]
            visualisation(L, titre="Quick Sort")  # Visualize after swap

    # Place the pivot in its correct position
    if L[left] > pivot:
        L[left], L[b - 1] = L[b - 1], L[left]
        visualisation(L, titre="Quick Sort")  # Visualize after pivot placement

    # Recursively sort the left partition (elements smaller than the pivot)
    quick(L, a, left)

    # Recursively sort the right partition (elements larger than the pivot)
    quick(L, left + 1, b)

    return L
