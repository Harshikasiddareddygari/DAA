def find_pair_sum_quadratic(arr, K):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == K:
                return True
    return False

def find_pair_sum_linear_log(arr, K):
    arr.sort()  # Sort the array
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == K:
            return True
        elif current_sum < K:
            left += 1
        else:
            right -= 1

    return False

# for O(n^2) algorithm
arr = [8, 4, 1, 6]
K = 10
print("Quadratic Algorithm:")
print(find_pair_sum_quadratic(arr, K))  # Output: True (4 and 6)

# O(nlogn) algorithm
arr = [8, 4, 1, 6]
K = 10
print("\nLinear Logarithmic Algorithm:")
print(find_pair_sum_linear_log(arr, K))  # Output: True (4 and 6)
