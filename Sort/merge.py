from visualisationTri import visualisation

def merge(L, time, sound, left=None, right=None):
    """
    Recursively implements the merge sort algorithm and visualizes the process.

    Parameters:
    L (list): The list to be sorted.
    time (float): The time delay between visualizations, in seconds.
    left (int, optional): The starting index of the current sublist. Defaults to None.
    right (int, optional): The ending index of the current sublist. Defaults to None.

    This function divides the list into smaller sublists, sorts each sublist, and then merges them back
    in sorted order using the `fusion` function. The sorting process is visualized at each step.
    """

    # Check if this is the first call to the merge function
    if not hasattr(merge, "initialized"):
        left = 0  # Start from the beginning of the list
        right = len(L)  # End at the last element
        merge.initialized = True  # Mark the merge initialization as complete

    # Base case: If the sublist has one or zero elements, it's already sorted
    if left >= right:
        return

    # Find the middle index of the current sublist
    mid = (left + right) // 2

    # Visualize the current state of the list
    visualisation(L, sound=sound, titre="Merge Sort", time=time)

    # Recursively sort the left half of the list
    merge(L, time, sound, left, mid)

    # Recursively sort the right half of the list
    merge(L, time, sound, mid + 1, right)

    # Visualize the list before merging the halves
    visualisation(L, sound=sound, titre="Merge Sort", time=time)

    # Merge the sorted halves back together
    mergeList(L, left, right, mid, time, sound)

    # Visualize the list after merging the halves
    visualisation(L, sound=sound,  titre="Merge Sort", time=time)

def mergeList(L, left, right, mid, time, sound):
    """
    Merges two sorted sublists (left and right halves) into a single sorted list.

    Parameters:
    L (list): The main list where the merged result will be placed.
    left (int): The starting index of the left half.
    right (int): The ending index of the right half.
    mid (int): The midpoint dividing the left and right halves.
    time (float): The time delay between visualizations, in seconds.

    The function compares elements from both the left and right halves of the list,
    placing the smaller elements into the main list `L` in sorted order.
    It visualizes the process after each modification.
    """

    # Create copies of the left and right halves of the list
    leftCopy = L[left: mid + 1]
    rightCopy = L[mid + 1: right + 1]

    # Initialize counters for left, right, and sorted portions of the list
    lCounter, rCounter = 0, 0
    sortedCounter = left

    # Merge elements from the left and right halves in sorted order
    while lCounter < len(leftCopy) and rCounter < len(rightCopy):
        visualisation(L, sound=sound, titre="Merge Sort", time=time)  # Visualize the current state
        if leftCopy[lCounter] <= rightCopy[rCounter]:
            L[sortedCounter] = leftCopy[lCounter]  # Place the smaller element from leftCopy
            lCounter += 1  # Move to the next element in leftCopy
        else:
            L[sortedCounter] = rightCopy[rCounter]  # Place the smaller element from rightCopy
            rCounter += 1  # Move to the next element in rightCopy
        sortedCounter += 1  # Move to the next position in the sorted portion

    # Append any remaining elements from leftCopy
    while lCounter < len(leftCopy):
        visualisation(L, sound=sound, titre="Merge Sort", time=time)  # Visualize the current state
        L[sortedCounter] = leftCopy[lCounter]
        lCounter += 1
        sortedCounter += 1

    # Append any remaining elements from rightCopy
    while rCounter < len(rightCopy):
        visualisation(L, sound=sound, titre="Merge Sort", time=time)  # Visualize the current state
        L[sortedCounter] = rightCopy[rCounter]
        rCounter += 1
        sortedCounter += 1
