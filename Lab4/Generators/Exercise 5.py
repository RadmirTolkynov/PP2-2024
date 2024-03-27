def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1

def main():
    try:
        n = int(input("Enter the value of n: "))

        countdown = countdown_generator(n)

        print(f"Countdown from {n} to 0:")
        for number in countdown:
            print(number, end=' ')

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
