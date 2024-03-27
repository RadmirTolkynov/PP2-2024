from functools import reduce

def multiply_list(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

my_list = [2, 3, 4, 5]
result = multiply_list(my_list)

print(f"The product of the numbers in the list {my_list} is: {result}")
