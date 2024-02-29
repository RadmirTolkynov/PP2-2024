import re

def replace_characters(input_string):
    pattern = re.compile(r'[ ,.]+')
    replaced_string = pattern.sub(':', input_string)
    print(f'Original string: {input_string}')
    print(f'Replaced string: {replaced_string}')

# Example usage:
input_string = "Hello World, Python. Replace spaces, commas and dots!"
replace_characters(input_string)
