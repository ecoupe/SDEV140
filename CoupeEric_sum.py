"""

Author:  Eric Coupe
Date written: 10/21/2024
Assignment:   Module02 Programming Assignment Part 2
Short Desc:   A program that receives a series of numbers from the user
              and allows the user to press the 'Enter' key to indicate
              they are finished providing inputs. After the 'Enter' key
              is pressed, the program will output the sum and average
              of the numbers.

"""

theSum = 0
count = 0

while True:
    number = input("Enter a number or press Enter to quit: ")
    if number == "":
        break
    number = float(number)
    theSum += number
    count += 1

print("The sum is", theSum)
if count > 0:
    print("The average is", theSum//count)