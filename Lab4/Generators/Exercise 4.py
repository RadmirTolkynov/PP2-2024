def squares_generator(a, b):
    for i in range(a, b + 1):
        yield i ** 2

def main():
    try:
        a = int(input("Enter the starting value (a): "))
        b = int(input("Enter the ending value (b): "))

        squares = squares_generator(a, b)

        print(f"Squares of numbers from {a} to {b}:")
        for square in squares:
            print(square, end=' ')

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
