import time
import math

def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000) 

    square_root = math.sqrt(number)

    return square_root

input_number = 25100
delay_milliseconds = 2123

result = calculate_square_root(input_number, delay_milliseconds)

print(f"Square root of {input_number} after {delay_milliseconds} milliseconds is {result}")
