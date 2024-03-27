def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i

def main():
    try:
        n = int(input("Enter the value of n: "))
        if n < 0:
            raise ValueError("Please enter a non-negative integer.")
        
        even_numbers = even_numbers_generator(n)
        result = ', '.join(map(str, even_numbers))
        
        print(f"Even numbers between 0 and {n}: {result}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
