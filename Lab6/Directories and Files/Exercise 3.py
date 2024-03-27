import os

def analyze_path(path):
    if os.path.exists(path):
        print(f"Path '{path}' exists.")

        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        print(f"Filename: {filename}")
        print(f"Directory: {directory}")

    else:
        print(f"Path '{path}' does not exist.")

if __name__ == "__main__":
    specified_path = input("Enter the path to analyze: ")

    analyze_path(specified_path)
