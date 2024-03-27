def parallelogram_area(base_length, height):
    area = base_length * height
    return area

def main():
    try:
        base_length = float(input("Enter the length of the base of the parallelogram: "))
        height = float(input("Enter the height of the parallelogram: "))

        area = parallelogram_area(base_length, height)
        print(f"The area of the parallelogram is: {area}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
