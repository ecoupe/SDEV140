"""

Author:  Eric Coupe
Date written: 10/21/2024
Assignment:   Module02 Programming Assignment Part 2
Short Desc:   A program that receives input of a non negative number.
              This number is then processed as a factorial with a 'FOR'
              loop. The factorial is then displayed to the user.
              There will be an error catch to ensure a positive integer
              is input. The function will loop until a positive integer
              is input.

"""
def non_negative_integer():
    while True:
        try:
            non_negative = int(input("Please enter a non-negative integer: "))
            if non_negative < 0:
                raise ValueError
            return non_negative
        except ValueError:
            print("Please enter a valid positive integer.")
non_negative = non_negative_integer()

factorial = 1

for i in range(1, non_negative + 1):
    factorial *= i

print(f"The factorial of {non_negative} is {factorial}.")
