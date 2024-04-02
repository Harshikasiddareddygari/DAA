import time
import random
import matplotlib.pyplot as plt

# Generate random array of 10000 elements
array_size = 10000
random_array = [random.randint(1, 1000) for _ in range(array_size)]

# Linear search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Binary search 
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#  measure execution time
search_key = int(input("Enter the search key: "))
linear_times = []
binary_times = []

for _ in range(5):
    start_time = time.time()
    linear_search(random_array, search_key)
    linear_times.append(time.time() - start_time)

    # Sort the array for binary search
    sorted_array = sorted(random_array)
    start_time = time.time()
    binary_search(sorted_array, search_key)
    binary_times.append(time.time() - start_time)

# Plotting the results
search_indices = list(range(1, 6))
plt.plot(search_indices, linear_times, label='Linear Search')
plt.plot(search_indices, binary_times, label='Binary Search')
plt.xlabel('Search Index')
plt.ylabel('Time (seconds)')
plt.title('Execution Time for Linear and Binary Searches')
plt.legend()
plt.show()
