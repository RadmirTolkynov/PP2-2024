def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print(f"Data written to '{file_path}' successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    file_path = input("Enter the path of the file to write the list: ")

    write_list_to_file(file_path, data)
