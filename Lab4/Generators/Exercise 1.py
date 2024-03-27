def squares_generator(N):
    for i in range(N + 1):
        yield i ** 2

def main():
    try:
        N = int(input("Enter the value of N: "))
        if N < 0:
            raise ValueError("Please enter a non-negative integer.")

        squares = squares_generator(N)
        result = list(squares)

        print(f"Squares of numbers up to {N}: {result}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
