def snake_to_camel(snake_case_string):
    words = snake_case_string.split('_')
    camel_case_string = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case_string

# Example usage:
snake_case_string = "hello_world_example"
camel_case_string = snake_to_camel(snake_case_string)

print(f'Snake case string: {snake_case_string}')
print(f'Camel case string: {camel_case_string}')
