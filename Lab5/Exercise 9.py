import re

def insert_spaces(input_string):
    modified_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    print(f'Original string: {input_string}')
    print(f'Modified string: {modified_string}')

# Example usage:
input_string = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
insert_spaces(input_string)
