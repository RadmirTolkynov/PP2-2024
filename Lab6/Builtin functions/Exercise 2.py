def count_upper_lower(string):
    # Initialize counters
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())

    return upper_count, lower_count

# Example usage:
input_string = "Hello World! This is a Python Program."

upper, lower = count_upper_lower(input_string)

print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
