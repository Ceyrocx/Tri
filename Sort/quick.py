from visualisationTri import visualisation

def repartition(L, Lrempl, start, end, time):
    """
    Fills a portion of the list `L` with the elements from `Lrempl`,
    while visualizing each modification.

    Args:
        L (list): The original list.
        Lrempl (list): The elements to insert into `L`.
        start (int): The start index in `L` for insertion.
        end (int): The end index in `L` for insertion.
        time (float): Delay between each visualization step.

    Returns:
        list: The updated list `L`.
    """

    y = 0  # Index for traversing `Lrempl`
    for i in range(start, end):
        visualisation(L, titre="Quick Sort", time=time)  # Visualize the current state
        L[i] = Lrempl[y]  # Insert the element from `Lrempl` into `L`
        y += 1  # Move to the next element in `Lrempl`
    return L

def quick(L, time, a=None, b=None):
    """
    Implements the Quick Sort algorithm with visualization at each step.

    Args:
        L (list): The list of elements to sort.
        time (float): Delay (in seconds) between each visualization step.
        a (int, optional): The starting index of the sublist to sort. Defaults to None.
        b (int, optional): The ending index of the sublist to sort. Defaults to None.

    Returns:
        list: The sorted list `L`.
    """

    # Initialize parameters on the first call
    if not hasattr(quick, "initialized"):
        a = 0  # Starting index of the list
        b = len(L)  # Ending index of the list
        quick.initialized = True  # Mark initialization as complete

    # Base case: Stop recursion if the sublist has fewer than 2 elements
    if b - a < 2:
        return L

    # Choose the last element as the pivot
    pivot = L[b - 1]
    Lsmall = []  # List for elements smaller than the pivot
    Llarge = []  # List for elements larger than the pivot

    # Partition elements around the pivot
    for i in range(a, b - 1):  # Iterate over elements except the pivot
        if L[i] < pivot:
            Lsmall.append(L[i])
        else:
            Llarge.append(L[i])

    # Reconstruct the list with smaller elements, the pivot, and larger elements
    L = repartition(L, Lsmall, a, a + len(Lsmall), time)  # Place smaller elements

    L[a + len(Lsmall)] = pivot  # Place the pivot at its correct position

    L = repartition(L, Llarge, a + len(Lsmall) + 1, b, time)  # Place larger elements

    posPivot = a + len(Lsmall)  # New position of the pivot

    # Recursive call to sort the left side (elements smaller than the pivot)
    quick(L, time, a=a, b=posPivot)

    # Recursive call to sort the right side (elements larger than the pivot)
    quick(L, time, a=posPivot + 1, b=b)

    visualisation(L, titre="Quick Sort", time=time)  # Visualize the current state
