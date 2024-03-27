import math

def degree_to_radian(degrees):
    radians = math.radians(degrees)
    return radians

def main():
    try:
        degree_input = float(input("Enter the degree value: "))
        radian_output = degree_to_radian(degree_input)
        print(f"Degree: {degree_input}\nRadian: {radian_output:.6f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
