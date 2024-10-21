"""

Author:  Eric Coupe
Date written: 10/21/2024
Assignment:   Module02 Practice Exercise 3-10
Short Desc:   A program that will take a purchase price of a car and
              output a table displaying a payment structure for the
              lifetime of the loan.


"""

flt_purchase_price = float(input("Enter the purchase price of the car: "))

ANNUAL_RATE = 0.12
MONTHLY_RATE = ANNUAL_RATE/12
DOWNPAYMENT_RATE = 0.10
TABLEFORMATSTRING = "{:2d}{:15.2f}{:15.2f}{:17.2f}{:17.2f}{:17.2f}"

monthly_payment = 0.05*flt_purchase_price
month = 1
balance = flt_purchase_price - (flt_purchase_price*DOWNPAYMENT_RATE)

print("Month Starting Balance Interest to Pay Principal to Pay Payment "
      " Ending Balance")

while balance > 0:
    if monthly_payment > balance:
        monthly_payment = balance
        interest = 0
    else:
        interest = balance*MONTHLY_RATE
    principal = monthly_payment - interest
    remaining = balance - monthly_payment

    print(TABLEFORMATSTRING.format(month, balance, interest, principal, monthly_payment, remaining))

    balance = remaining
    month = month + 1
