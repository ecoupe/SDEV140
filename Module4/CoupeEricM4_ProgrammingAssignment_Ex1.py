"""
Author:  Eric Coupe
Date written: 11/18/2024
Assignment:   Module04 Programming Assignment Ex1
Short Desc:   This program requests a number greater than 1. It has a
              while loop to determine if it was a valid integer. It then
              creates a list of numbers beginning with 2 until the input
              number is reached. This list is then passed through a 
              function that determines if the numbers in the list are
              prime or not. Finally it outputs the list of prime
              numbers between 2 and the input number.

"""

def check_for_prime(number):
    # Sets the input to prime until determined otherwise
    is_prime = True
    
    # Checks if any numbers in range of 2 to input-1 are divisible and
    # have remainders using 'modulo' operator. If there is a remainder
    # the loop breaks and the next number in the range is tested
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break
    
    # Display the prime numbers all on one line instead of new lines
    if is_prime:
        print(number, end=" ")

def main():
    # Get user input and uses a while loop to ensure valid input
    while True:
        try:
            number = int(input("Enter an integer greater than 1: "))
            if number > 1:
                break
            print("Please enter a number greater than 1.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Creates a list of numbers from 2 to the input number
    numbers = list(range(2, number + 1))
    
    # Prints on a new line for readability. Not necessary but I like it
    print(f"\nPrime numbers less than or equal to {number} are:")
    
    # Call the 'check_for_prime' function to check each number 
    # in the list for primality
    for num in numbers:
        check_for_prime(num)
    
# Run the program
if __name__ == "__main__":
    main()