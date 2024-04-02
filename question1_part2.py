import time
import random
import matplotlib.pyplot as plt

# Selection sort algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Insertion sort algorithm
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#  1000 random integers between 1 and 10000
random_numbers = [random.randint(1, 10000) for _ in range(1000)]

# Measure time taken for sorting using different algorithms
start_time = time.time()
sorted_numbers_built_in = sorted(random_numbers)
time_taken_built_in = time.time() - start_time

start_time = time.time()
selection_sort(random_numbers.copy())
time_taken_selection = time.time() - start_time

start_time = time.time()
insertion_sort(random_numbers.copy())
time_taken_insertion = time.time() - start_time

# Plotting the results
labels = ['Built-in Sort', 'Selection Sort', 'Insertion Sort']
times = [time_taken_built_in, time_taken_selection, time_taken_insertion]

plt.bar(labels, times)
plt.xlabel('Sorting Algorithm')
plt.ylabel('Time (seconds)')
plt.title('Time Taken to Sort 1000 Random Integers')
plt.show()
