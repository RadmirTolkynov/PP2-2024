import re

def match_pattern(input_string):
    pattern = re.compile(r'ab{2,3}')
    match = pattern.fullmatch(input_string)
    
    if match:
        print(f'The string "{input_string}" matches the pattern.')
    else:
        print(f'The string "{input_string}" does not match the pattern.')

# Example usage:
input_string1 = "abb"
input_string2 = "abbb"
input_string3 = "abbbb"
input_string4 = "ac"

match_pattern(input_string1)
match_pattern(input_string2)
match_pattern(input_string3)
match_pattern(input_string4)
