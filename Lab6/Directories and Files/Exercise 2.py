import os

def check_access(path):
    if os.path.exists(path):
        print(f"Path '{path}' exists.")

        if os.access(path, os.R_OK):
            print(f"Read access to '{path}' is granted.")
        else:
            print(f"Read access to '{path}' is denied.")

        if os.access(path, os.W_OK):
            print(f"Write access to '{path}' is granted.")
        else:
            print(f"Write access to '{path}' is denied.")
        if os.access(path, os.X_OK):
            print(f"Execute access to '{path}' is granted.")
        else:
            print(f"Execute access to '{path}' is denied.")

    else:
        print(f"Path '{path}' does not exist.")

if __name__ == "__main__":
    specified_path = input("Enter the path to check access: ")

    check_access(specified_path)
