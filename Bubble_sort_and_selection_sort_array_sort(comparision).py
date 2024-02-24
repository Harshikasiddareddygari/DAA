import time
import random

def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return swaps

def selection_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps += 1
    return swaps

#  measure execution time and swaps
def measure_time_and_swaps(sort_function, arr):
    start_time = time.time()
    swaps = sort_function(arr)
    end_time = time.time()
    return (end_time - start_time) * 1000, swaps

#  user input 
list_size = int(input("Enter the size of the list: "))

# Generate a random list of numbers for testing
arr = [random.randint(1, 1000) for _ in range(list_size)]

#  copies for sorting
arr_bubble = arr.copy()
arr_selection = arr.copy()
arr_sorted = arr.copy()

# compare execution time and swaps for Bubble Sort
bubble_sort_time, bubble_sort_swaps = measure_time_and_swaps(bubble_sort, arr_bubble)
print("\nBubble Sort:")
print(f"Sorted List: {arr_bubble}")
print(f"Execution Time: {bubble_sort_time:.6f} milliseconds")
print(f"Swaps: {bubble_sort_swaps}")

# compare execution time and swaps for Selection Sort
selection_sort_time, selection_sort_swaps = measure_time_and_swaps(selection_sort, arr_selection)
print("\nSelection Sort:")
print(f"Sorted List: {arr_selection}")
print(f"Execution Time: {selection_sort_time:.6f} milliseconds")
print(f"Swaps: {selection_sort_swaps}")

# compare execution time for sorted()
sorted_time, _ = measure_time_and_swaps(sorted, arr_sorted)
print("\nsorted():")
print(f"Sorted List: {arr_sorted}")
print(f"Execution Time: {sorted_time:.6f} milliseconds")

# Compare the algorithms
if bubble_sort_time < selection_sort_time and bubble_sort_time < sorted_time:
    print("\nBubble Sort is the fastest.")
elif selection_sort_time < bubble_sort_time and selection_sort_time < sorted_time:
    print("\nSelection Sort is the fastest.")
else:
    print("\nsorted() is the fastest.")
