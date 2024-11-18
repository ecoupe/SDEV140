"""

Author:  Eric Coupe
Date written: 11/16/2024
Assignment:   Module04 Practice Exercise 5-7
Short Desc:   A program that opens a text file with data and sorts the
              text in alphabetical order.

"""
with open("text.txt", 'r') as list_of_words:
    text = list_of_words.read().split()

all_in_order = sorted(set(text))

for word in all_in_order:
    print(word)

