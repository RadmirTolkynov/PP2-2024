def is_palindrome(input_string):
    cleaned_string = ''.join(input_string.lower().split())

    return cleaned_string == cleaned_string[::-1]

user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
