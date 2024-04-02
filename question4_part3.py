def segregate_0s_1s(arr):
    """Segregates 0s to the left and 1s to the right in a binary array.

    Args:
        arr: The input binary array containing 0s and 1s.

    Returns:
        The segregated array.
    """

    left = 0
    right = len(arr) - 1

    while left < right:
        while arr[left] == 0 and left < right:
            left += 1
        while arr[right] == 1 and left < right:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

# Get user input for the array
arr = []
while True:
    num_str = input("Enter 0 or 1 (or 'done' to finish): ")
    if num_str == 'done':
        break
    if num_str not in ('0', '1'):
        print("Invalid input. Please enter 0 or 1.")
        continue
    num = int(num_str)
    arr.append(num)

# Segregate the array and print the result
segregated_arr = segregate_0s_1s(arr.copy())  # Segregate a copy to avoid modifying the original
print("Segregated array:", segregated_arr)
