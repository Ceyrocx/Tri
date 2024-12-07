import argparse
from random import shuffle
from xmlrpc.client import boolean

from Sort.bogo import bogo
from Sort.bubble import bubble
from Sort.frequency import frequency
from Sort.quick import quick
from Sort.selection import selection
from Sort.merge import merge
from Sort.insertion import insertion

# Dictionary associating algorithm names with their respective functions
dictTri = {
    "bogo": bogo,    # Bogo sort algorithm
    "bubble": bubble,  # Bubble sort algorithm
    "frequency": frequency,  # Frequency sort algorithm
    "quick": quick,  # Quick sort algorithm
    "selection": selection,  # Selection sort algorithm
    "merge": merge,  # Merge sort algorithm
    "insertion": insertion,  # Insertion sort algorithm
}

def run(amount, tri, time, sound):
    """
    Generates a list of unique random integers and applies the specified sorting algorithm to it.
    Visualizes the sorting process using a time delay and optional sound.

    Parameters:
    amount (int): The number of unique elements to generate and sort.
    tri (str): The name of the sorting algorithm to use (one of 'bogo', 'bubble', 'frequency', 'quick', etc.).
    time (float): The delay time between visualizations during sorting, in seconds.
    sound (bool): A flag indicating whether sound should be played during the visualization.

    Returns:
    None: This function does not return a value; it calls the sorting function from dictTri.

    Notes:
    - The list is first shuffled to ensure randomness before sorting begins.
    - The sorting function is chosen based on the value of `tri`.
    - The list will be sorted according to the chosen algorithm, and the process is visualized.
    """
    # Create a list of unique integers from 1 to `amount`
    L = [i for i in range(1, amount + 1)]
    shuffle(L)  # Randomly shuffle the list `L` to disorder it

    # Validate if the sorting algorithm is valid
    if tri.lower() not in dictTri:
        print(f"Error: '{tri}' is not a valid sorting algorithm. Please choose from {list(dictTri.keys())}.")
        return

    # Call the appropriate sorting function based on the selected algorithm
    dictTri[tri.lower()](L, time, sound)


if __name__ == "__main__":
    # Initialize the argument parser for command-line arguments
    parser = argparse.ArgumentParser(description="An example script with command-line arguments for sorting visualizations.")

    # Define the arguments
    parser.add_argument("-n", "--amount", type=int, default=5, help="Number of elements to sort.")
    parser.add_argument("-t", "--tri", type=str, default="bogo", help="Sorting algorithm to use (e.g., 'bogo', 'bubble', 'selection').")
    parser.add_argument("-s", "--speed", type=float, default=0.01, help="Speed of the sorting visualization (time delay in seconds).")
    parser.add_argument("-m", "--sound", type=str, default="False", help="Activate sound during visualization ('True' or 'False').")

    # Parse the arguments
    args = parser.parse_args()

    # Convert the string 'True'/'False' to a boolean
    sound = args.sound.lower() == 'true'

    # Call the function with the obtained parameters
    run(amount=args.amount, tri=args.tri, time=args.speed, sound=sound)
