import re

def camel_to_snake(camel_case_string):
    snake_case_string = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_case_string).lower()
    return snake_case_string

