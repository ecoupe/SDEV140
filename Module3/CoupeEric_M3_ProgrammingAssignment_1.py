"""
Author:  Eric Coupe
Date written: 11/7/2024
Assignment:   Module03 Programming Assignment Part 1
Short Desc:   A program that asks for a series of single-digit numbers.
              It will then loop through the input changing characters
              into integers, then adding the input together.

"""
ask_for_numbers = input("Please input a series of single digit numbers with " \
                        "no spaces: ")

# initializing variable at 0
sum_of_input = 0

# for loop will go through user input and convert each letter of the
# string into an integer. Then it will add each integer together and
# update the 'sum_of_input' variable
for characters in ask_for_numbers:
    sum_of_input += int(characters)

print(f"The sum of the single-digits you input is: {sum_of_input}")
