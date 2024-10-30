"""

Author:  Eric Coupe
Date written: 10/21/2024
Assignment:   Module01 Programming Assignment part2
Short Desc:   A program that calculates the total amount of a meal purchased at a restaurant. 
              The program will ask the user to enter the charge for the food, then 
              calculate the amounts of a 18 percent tip and 7 percent sales tax, then print the results. 


"""
food_charge = float(input("Please enter the charge for your meal: "))
server_tip = food_charge*0.18
sales_tax = food_charge*0.07
total_bill = food_charge+server_tip+sales_tax

# the outputs are formatted to limit float values to 2 decimals
print(f"The tip of 18% is: {server_tip:,.2f}")
print(f"The sales tax is: {sales_tax:,.2f}")
print(f"The total bill is: {total_bill:,.2f}")
