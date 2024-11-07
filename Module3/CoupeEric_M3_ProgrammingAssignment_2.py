"""
Author:  Eric Coupe
Date written: 11/7/2024
Assignment:   Module03 Programming Assignment Part 2
Short Desc:   A program that opens a file then asks the user for 
              a number of times they want a random number generated. 
              The program will generat these numbers, output them to the
              screen, and write it to a file.

"""

import random   # adds the random library to the program #

# opens the file in append mode to preserve data and not overwrite each
# program execution 
open_text_file = open('randomintegers.txt', 'a')

print("This program will write a specified amount of random numbers.")
user_defined_input = int(input("Please choose the amount: "))

# for loop will run for a defined amount of times input by the user #
for count in range(user_defined_input):
    # random numbers will generate between 1 and 500 #
    number = random.randint(1, 500)
    # convert int to str to write in the file #
    open_text_file.write(str(number) + '\n')
    print(number)

open_text_file.close()
