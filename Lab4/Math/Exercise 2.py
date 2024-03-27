def trapezoid_area(height, base1, base2):
    area = 0.5 * (base1 + base2) * height
    return area

def main():
    try:
        height = float(input("Enter the height of the trapezoid: "))
        base1 = float(input("Enter the length of the first base: "))
        base2 = float(input("Enter the length of the second base: "))

        area = trapezoid_area(height, base1, base2)
        print(f"The area of the trapezoid is: {area}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
