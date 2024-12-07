from visualisationTri import visualisation

def repartition(L, Lrempl, start, end, time, sound):
    """
    Fills a portion of the list `L` with the elements from `Lrempl`,
    while visualizing each modification.

    Args:
        L (list): The original list.
        Lrempl (list): The elements to insert into `L`.
        start (int): The start index in `L` for insertion.
        end (int): The end index in `L` for insertion.
        time (float): Delay between each visualization step.
        sound (bool): Whether to play a sound during visualization.

    Returns:
        list: The updated list `L`.
    """

    y = 0  # Index for traversing `Lrempl`
    for i in range(start, end):
        L[i] = Lrempl[y]  # Insert the element from `Lrempl` into `L`
        visualisation(L, sound=sound, titre="Quick Sort", time=time)  # Visualize the current state
        y += 1  # Move to the next element in `Lrempl`
    return L

def quick(L, time, sound, a=None, b=None):
    """
    Sorts a list using the Quick Sort algorithm and visualizes each step.

    Args:
        L (list): The list of elements to sort.
        time (float): Delay (in seconds) between each visualization step.
        sound (bool): Whether to play a sound during visualization.
        a (int, optional): The starting index of the sublist to sort. Defaults to 0.
        b (int, optional): The ending index of the sublist to sort. Defaults to the length of the list.

    Returns:
        list: The sorted list `L`.
    """
    # Initialize parameters on the first call
    if a is None:
        a = 0
    if b is None:
        b = len(L)

    # Base case: Stop recursion if the sublist has fewer than 2 elements
    if b - a < 2:
        return L

    # Choose the last element as the pivot
    pivot = L[b - 1]

    # Partition the list into elements smaller and larger than the pivot
    left = a
    right = b - 1

    while left < right:
        if L[left] < pivot:
            left += 1  # Left element is in the correct position
        else:
            right -= 1  # Reduce the right boundary
            L[left], L[right] = L[right], L[left]  # Swap to move the larger element to the right

    # Place the pivot in its correct position
    L[left], L[b - 1] = L[b - 1], L[left]

    # Visualize the list after placing the pivot
    visualisation(L, sound=sound, titre="Quick Sort", time=time)

    # Recursive call to sort the left part of the list (elements smaller than the pivot)
    quick(L, time, sound, a, left)

    # Recursive call to sort the right part of the list (elements larger than the pivot)
    quick(L, time, sound, left + 1, b)

    return L