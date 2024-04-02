def print_highest_k_values(arr, k):
    # Print the highest k values from the sorted array
    for i in range(len(arr) - 1, len(arr) - 1 - k, -1):
        print(arr[i])

# Taking user input for the array and k
arr = list(map(int, input("Enter space-separated elements of the array: ").split()))
k = int(input("Enter the value of k (number of highest values to print): "))

# Sort the array in ascending order
arr.sort()

# Print the highest k values
print_highest_k_values(arr, k)
