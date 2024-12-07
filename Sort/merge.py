from visualisationTri import visualisation

def merge(L, time, sound, left=None, right=None):
    """
    Sorts a list using the Merge Sort algorithm and visualizes the process.

    Parameters:
    L (list): The list to be sorted.
    time (float): The time delay between visualizations, in seconds.
    sound (bool): Whether to play a sound during visualization.
    left (int, optional): The starting index of the current sublist. Defaults to None.
    right (int, optional): The ending index of the current sublist. Defaults to None.

    This function divides the list into smaller sublists, sorts each sublist, and then merges them back
    in sorted order using the `mergeList` function. The sorting process is visualized at key steps.
    """

    # Initialize the left and right indices on the first call
    if left is None and right is None:
        left = 0  # Start from the beginning of the list
        right = len(L) - 1  # End at the last element

    # Base case: if the sublist has one or zero elements, it's already sorted
    if left >= right:
        return

    # Find the middle index to divide the list
    mid = (left + right) // 2

    # Recursively sort the left half of the list
    merge(L, time, sound, left, mid)

    # Recursively sort the right half of the list
    merge(L, time, sound, mid + 1, right)

    # Merge the sorted halves back together
    mergeList(L, left, right, mid, time, sound)

    # Visualize the list after merging
    visualisation(L, sound=sound, titre="Merge Sort", time=time)


def mergeList(L, left, right, mid, time, sound):
    """
    Merges two sorted sublists (left and right halves) into a single sorted list.

    Parameters:
    L (list): The main list where the merged result will be placed.
    left (int): The starting index of the left half.
    right (int): The ending index of the right half.
    mid (int): The midpoint dividing the left and right halves.
    time (float): The time delay between visualizations, in seconds.
    sound (bool): Whether to play a sound during visualization.

    This function compares elements from both the left and right halves of the list,
    placing the smaller elements into the main list `L` in sorted order.
    It visualizes the process after each modification.
    """

    # Create copies of the left and right halves
    leftCopy = L[left:mid + 1]
    rightCopy = L[mid + 1:right + 1]

    # Initialize counters for the left, right, and sorted portions of the list
    lCounter, rCounter = 0, 0
    sortedCounter = left

    # Merge elements from the left and right halves in sorted order
    while lCounter < len(leftCopy) and rCounter < len(rightCopy):
        if leftCopy[lCounter] <= rightCopy[rCounter]:
            L[sortedCounter] = leftCopy[lCounter]  # Insert from left half
            lCounter += 1
        else:
            L[sortedCounter] = rightCopy[rCounter]  # Insert from right half
            rCounter += 1
        sortedCounter += 1
        visualisation(L, sound=sound, titre="Merge Sort", time=time)  # Visualize after each insertion

    # Append any remaining elements from leftCopy
    while lCounter < len(leftCopy):
        L[sortedCounter] = leftCopy[lCounter]
        lCounter += 1
        sortedCounter += 1
        visualisation(L, sound=sound, titre="Merge Sort", time=time)

    # Append any remaining elements from rightCopy
    while rCounter < len(rightCopy):
        L[sortedCounter] = rightCopy[rCounter]
        rCounter += 1
        sortedCounter += 1
        visualisation(L, sound=sound, titre="Merge Sort", time=time)
