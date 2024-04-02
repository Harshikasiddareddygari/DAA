def string_to_integer(s):
    # Base case: if the string is empty, return 0
    if len(s) == 0:
        return 0
   
    return string_to_integer(s[:-1]) * 10 + int(s[-1])

# Test the function
input_string = input("Enter a string of digits: ")
result = string_to_integer(input_string)
formatted_result = "{:,}".format(result)  # Format with commas
print("Integer representation:", formatted_result)
