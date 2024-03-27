import math

def regular_polygon_area(sides, length):
    area = (sides * length**2) / (4 * math.tan(math.pi / sides))
    return area

def main():
    try:
        sides = int(input("Enter the number of sides of the regular polygon: "))
        length = float(input("Enter the length of a side: "))

        area = regular_polygon_area(sides, length)
        print(f"The area of the regular polygon is: {area}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
