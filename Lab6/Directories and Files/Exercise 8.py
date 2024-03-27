import os

def delete_file(file_path):
    try:

        if os.path.exists(file_path):
            print(f"File '{file_path}' exists.")

            if os.access(file_path, os.W_OK):

                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            else:
                print(f"Write access to '{file_path}' is denied. Cannot delete the file.")

        else:
            print(f"File '{file_path}' does not exist. Cannot delete.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    specified_path = input("Enter the path of the file to delete: ")

    delete_file(specified_path)
