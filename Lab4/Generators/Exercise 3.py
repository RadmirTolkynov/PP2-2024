def divisible_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def main():
    try:
        n = int(input("Enter the value of n: "))
        if n < 0:
            raise ValueError("Please enter a non-negative integer.")
        
        result_generator = divisible_by_3_and_4_generator(n)

        print(f"Numbers divisible by 3 and 4 between 0 and {n}:")
        for num in result_generator:
            print(num, end=' ')

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
