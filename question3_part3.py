def sort_ascending(arr):

  n = len(arr)
  for i in range(n):
    # Find the index of the minimum element in the unsorted part
    min_index = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_index]:
        min_index = j

    # Swap the found minimum element with the first element of the unsorted part
    if min_index != i:
      arr[i], arr[min_index] = arr[min_index], arr[i]

  return arr

# Get user input for the array
arr = []
while True:
  num_str = input("Enter an integer (or 'done' to finish): ")
  if num_str == 'done':
    break
  try:
    num = int(num_str)
    arr.append(num)
  except ValueError:
    print("Invalid input. Please enter an integer.")

# Sort the array and print the result
sorted_arr = sort_ascending(arr.copy())  # Sort a copy to avoid modifying the original
print("Sorted array:", sorted_arr)
