import time
import random
import matplotlib.pyplot as plt

# Iterative approach
def sum_iterative(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

# Recursive approach
def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)

# execution time for random N values
n_values = [random.randint(1, 1000) for _ in range(10)]  # Random N values
iterative_times = []
recursive_times = []

for n in n_values:
    start_time = time.time()
    sum_iterative(n)
    iterative_times.append(time.time() - start_time)

    start_time = time.time()
    sum_recursive(n)
    recursive_times.append(time.time() - start_time)

# Plotting the results
plt.plot(n_values, iterative_times, label='Iterative')
plt.plot(n_values, recursive_times, label='Recursive')
plt.xlabel('N Values')
plt.ylabel('Time (seconds)')
plt.title('Execution Time for Sum of First N Natural Numbers (Random N Values)')
plt.legend()
plt.show()
