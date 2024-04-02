def merge(arr, temp, left, mid, right):
    inv_count = 0

    i = left  # Initial index of first subarray
    j = mid + 1  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
            inv_count += (mid - i + 1)  # Count inversions
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inv_count

def merge_sort(arr, temp, left, right):
    inv_count = 0

    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort(arr, temp, left, mid)
        inv_count += merge_sort(arr, temp, mid + 1, right)
        inv_count += merge(arr, temp, left, mid, right)

    return inv_count

def inversion_count(arr):
    n = len(arr)
    temp = [0] * n
    return merge_sort(arr, temp, 0, n - 1)

# Example usage:
A = [10, 1, 2, 4, 13, 9, 5]
print("The number of inversions:", inversion_count(A))
