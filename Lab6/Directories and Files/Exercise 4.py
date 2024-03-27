def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"The number of lines in the file '{file_path}' is: {line_count}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    file_path = input("Enter the path of the text file: ")
    count_lines(file_path)
