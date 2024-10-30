"""

Author:  Eric Coupe
Date written: 10/21/2024
Assignment:   Module01 Programming Assignment part1
Short Desc:   A program that converts user inputted
              temperature from Celcius into Fahrenheit. 


"""

temp_celsius = float(input("Please enter the temperature in Celsius: "))
temp_fahrenheit = ((9/5)*(temp_celsius))+32

print(f"{temp_celsius} degrees Celsius is {temp_fahrenheit:,.2f} degrees" +
      " in Fahrenheit.")
