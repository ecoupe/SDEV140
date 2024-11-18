"""
Author:  Eric Coupe
Date written: 11/18/2024
Assignment:   Module04 Programming Assignment Ex2
Short Desc: This program displays the top 3 most expensive items from a
            dictionary of sample data. A dictionary is created with the
            sample data. A variable is declared to sort through the
            items. It uses a lambda function to sort the list by price.
            The order is reversed so it is organized descending from
            largest number to smallest. It is then sliced by the top 3
            of the list.

"""

shop_items = {
    'Apple': 0.50,
    'Banana': 0.20,
    'Mango': 0.99,
    'Coconut': 2.99,
    'Pineapple': 3.99
}

top_three = sorted(shop_items.items(), key=lambda x: x[1], reverse=True)[:3]

print("Top 3 most expensive items: ")
for item, price in top_three:
    print(f"{item}: ${price}")