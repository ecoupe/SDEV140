def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def display_primes_up_to(limit):
    """Display all prime numbers up to a specified limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    """Main function to run the program."""
    while True:
        try:
            user_input = int(input("Enter an integer greater than 1: "))
            if user_input > 1:
                break
            else:
                print("Please enter a number greater than 1.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    primes = display_primes_up_to(user_input)
    print(f"Prime numbers less than or equal to {user_input}: {primes}")

if __name__ == "__main__":
    main()
