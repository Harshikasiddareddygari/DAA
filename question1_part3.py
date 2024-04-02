def find_pair_with_sum(nums, target):


    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return num, complement
        seen.add(num)

    return None

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

# Get user input for the target sum
while True:
    try:
        target = int(input("Enter the target sum: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Find the pair and print the result
pair = find_pair_with_sum(nums, target)
if pair:
    print("Pair found:", pair)
else:
    print("Pair not found")
