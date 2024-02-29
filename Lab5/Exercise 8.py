import re

def split_at_uppercase(input_string):
    split_parts = re.findall('[A-Z][^A-Z]*', input_string)
    print(f'String: {input_string}')
    print(f'Split parts: {split_parts}')

# Example usage:
input_string = "SplitThisStringAtUpperCaseLetters"
split_at_uppercase(input_string)
