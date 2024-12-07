# **Sorting Algorithms with Visualization**

Welcome to this project that implements several classic sorting algorithms in Python, with dynamic visualizations using Matplotlib. The goal is to help understand the inner workings of these sorting algorithms through visual animations.

## **Features**

- **Available Sorting Algorithms**:
  - **Bogo Sort**: An inefficient but amusing algorithm that randomly shuffles the elements until they are sorted.
  - **Bubble Sort**: A more traditional algorithm that compares adjacent elements and swaps them if needed, sorting the list iteratively.
  - **Selection Sort**: An algorithm that repeatedly selects the smallest element from the unsorted portion and places it in the sorted portion.
  - **Insertion Sort**: An algorithm that builds the final sorted array one item at a time.
  - **Quick Sort**: A divide-and-conquer algorithm that partitions the list and recursively sorts the partitions.
  - **Merge Sort**: Another divide-and-conquer algorithm that divides the list into halves and sorts each recursively.
  - **Frequency Sort**: A custom sorting algorithm that sorts based on the frequency of elements.

- **Dynamic Visualization**:
  - The algorithms are accompanied by real-time graphical visualizations showing each step of the sorting process.
  - Bars representing the elements are updated as the algorithm performs comparisons and swaps.

- **Configurable Parameters**:
  - Choose the number of elements to sort.
  - Select the sorting algorithm you want to visualize.
  - Control the speed of the animation.

## **Installation**

### Prerequisites
Make sure you have Python installed (version 3.6 or later). Then, you need to install the Python dependencies listed in the `requirements.txt` file.

1. Clone this repository:ns, feel free to open an issue or contact me directly.
    git clone: https://github.com/Ceyrocx/tri.git

2. Install the required dependencies: pip install -r requirements.txt

### Dependencies

The main dependencies for this project are:

- `matplotlib`: For graphical visualization of the sorting algorithms.
- `numpy`: For managing numerical sequences (used for axis creation in the graphs).

## **Usage**

This project can be run from the command line with arguments to configure the algorithm, number of elements to sort, and animation speed.

### Basic Command

- **Sort 100 elements using the Bubble Sort algorithm with a 0.05-second delay between each step**:
    python run.py -n 100 -t "bubble" -s 0.05
- **Sort 20 elements using the Selection Sort algorithm with a 0.000001-second delay**:
    python run.py -n 20 -t "selection" -s 0.000001

### Available Options

- `-n`, `--amount`: Number of elements to sort (default: 5).
- `-t`, `--tri`: Sorting algorithm to use (`bogo`, `bubble`, `selection`, `insertion`, `quick`, `merge`, `frequency`; default: `bogo`).
- `-s`, `--speed`: Time delay (in seconds) between each visualization step (default: 0.01).
- `-m`, `--sound`: Enable or disable sound during visualization (default: False).

## **Project Organization**

- **`run.py`**: Entry point for the project, handles command-line arguments and starts the selected sorting algorithm.
- **`bogo.py`**: Contains the implementation and visualization of the Bogo Sort algorithm.
- **`bubble.py`**: Contains the implementation and visualization of the Bubble Sort algorithm.
- **`selection.py`**: Contains the implementation and visualization of the Selection Sort algorithm.
- **`insertion.py`**: Contains the implementation and visualization of the Insertion Sort algorithm.
- **`quick.py`**: Contains the implementation and visualization of the Quick Sort algorithm.
- **`merge.py`**: Contains the implementation and visualization of the Merge Sort algorithm.
- **`frequency.py`**: Contains the implementation and visualization of the Frequency Sort algorithm.
- **`visualisationTri.py`**: Provides the functions for visualizing the sorting algorithms.
- **`requirements.txt`**: A file listing the necessary dependencies for the project.

## **Functionality Overview**

### Sorting Algorithms

Each algorithm sorts the list and updates the visualization in real-time. The primary functions for sorting are implemented as follows:

- **Bogo Sort**: Randomly shuffles elements until the list is sorted.
- **Bubble Sort**: Repeatedly compares adjacent elements and swaps them if they are in the wrong order.
- **Selection Sort**: Selects the smallest unsorted element and places it in the correct position.
- **Insertion Sort**: Inserts each element into its correct position in the sorted portion of the list.
- **Quick Sort**: Partitions the list and recursively sorts each part.
- **Merge Sort**: Recursively divides the list into halves and sorts each part.

Each sorting function visualizes the state of the list after each step, with a delay for better understanding.

### Visualization

- **Bars**: Each element of the list is represented by a bar, where the height of the bar corresponds to the value of the element.
- **Color Change**: As the algorithm progresses, the bars change color to indicate comparisons and swaps.
- Green: A bar has changed.
- Red: Final sorted state.
- **Sound**: Optionally, a beep sound plays each time an element changes, with a frequency based on the height of the bar.
- The frequency increases as the height of the bar increases, making the sound distinctive and easily recognizable.

### Sound

- The `winsound.Beep` function is used to play a sound when an element changes position during sorting.
- The frequency of the sound is calculated dynamically to be both audible and distinct for each change, with the formula ensuring that the beep remains clear and easily distinguishable.

### Parameters for `visualisationTri.py`

- **`L`**: List of elements to be sorted.
- **`time`**: Delay between each step of the visualization (in seconds).
- **`sound`**: Whether to enable sound during the visualization.
- **`titre`**: Title for the visualization (optional).
- **`nbTest`**: Test iteration number for display (optional).

## **Future Improvements**

Here are some ideas for enhancing this project:

- Add additional sorting algorithms like Heap Sort, Radix Sort, and Tim Sort.
- Improve the user interface to make the visualizations more interactive (e.g., allow pausing and resuming the sorting process).
- Customize the colors and animations for better visual appeal.
- Add unit tests to ensure that each sorting algorithm functions correctly.

## **Contact**

If you have any questions or suggestions, feel free to open an issue or contact me directly.
