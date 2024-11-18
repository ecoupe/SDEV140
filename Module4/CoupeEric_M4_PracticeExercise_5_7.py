"""

Author:  Eric Coupe
Date written: 11/16/2024
Assignment:   Module04 Practice Exercise 5-7
Short Desc:   A program that opens a text file with data and sorts the
              text in alphabetical order.

"""
file_name = input("Enter the input file name: ")

# used 'with' keyword to automatically close the file when program ends
with open(file_name, 'r') as list_of_words:
    text = list_of_words.read().split() #splits the list into individual
                                        #words

#set function removes duplicates, list converts it back into a list for
#the next line to sort
all_in_order = list(set(text))
all_in_order.sort()

for word in all_in_order:
    print(word)

