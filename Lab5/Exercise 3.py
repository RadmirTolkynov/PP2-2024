import re

def find_sequences(input_string):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    matches = pattern.findall(input_string)

    if matches:
        print(f'Sequences found: {matches}')
    else:
        print('No sequences found. ')
    
# Example usage:
input_string1 = "hello_world"
input_string2 = "Python_is_fantastic"
input_string3 = "No_Underscore_here"

find_sequences(input_string1)
find_sequences(input_string2)
find_sequences(input_string3)