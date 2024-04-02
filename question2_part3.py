def find_max_product_pair(nums):
  
    if len(nums) < 2:
        return None  # Handle empty or single-element arrays

    max_product = float('-inf')  # Initialize with negative infinity
    max_pair = None

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            product = nums[i] * nums[j]
            if product > max_product:
                max_product = product
                max_pair = (nums[i], nums[j])

    return max_pair

# Get user input for the array
nums = []
while True:
    num_str = input("Enter an integer (or 'done' to finish): ")
    if num_str == 'done':
        break
    try:
        num = int(num_str)
        nums.append(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Find the pair with maximum product and print the result
pair = find_max_product_pair(nums)
if pair:
    print("Pair with maximum product:", pair)
else:
    print("Array is empty or has less than two elements")
