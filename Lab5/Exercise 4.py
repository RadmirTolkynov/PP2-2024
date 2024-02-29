import re

def find_sequences(input_string):
    pattern = re.compile(r'[A-Z][a-z]+')
    matches = pattern.findall(input_string)
    
    if matches:
        print(f'Sequences found: {matches}')
    else:
        print('No sequences found.')

# Example usage:
input_string1 = "HelloWorld"
input_string2 = "PythonIsGreat"
input_string3 = "NoUpperCaseHere"

find_sequences(input_string1)
find_sequences(input_string2)
find_sequences(input_string3)