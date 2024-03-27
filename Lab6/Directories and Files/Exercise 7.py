def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source_file, open(destination_path, 'w') as destination_file:
        content = source_file.read()
        destination_file.write(content)

    print(f"Contents of '{source_path}' copied to '{destination_path}' successfully.")

if __name__ == "__main__":
    source_file_path = input("Enter the path of the source file: ")
    destination_file_path = input("Enter the path of the destination file: ")

    copy_file(source_file_path, destination_file_path)
