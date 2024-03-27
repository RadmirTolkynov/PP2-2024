import os

def list_directories(path):
    print("List of Directories:")
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            print(entry)

def list_files(path):
    print("\nList of Files:")
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path):
            print(entry)

def list_all(path):
    print("\nList of All Directories and Files:")
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        print(entry)

if __name__ == "__main__":
    specified_path = input("Enter the path to list directories and files: ")

    if os.path.exists(specified_path):
        list_directories(specified_path)
        list_files(specified_path)
        list_all(specified_path)
    else:
        print("Invalid path. Please provide a valid path.")
