"""

Author:  Eric Coupe
Date written: 11/16/2024
Assignment:   Module04 Practice Exercise 5-7
Short Desc:   A program that opens a text file with data and places the
              text in alphabetical order and shows the frequency the
              word occurs.
"""
concordance = input("Enter the input file name: ")

#uses keyword 'with' to automatically close the file when program ends
with open(concordance, 'r') as file:
    text = file.read().split() #reads and splits data

#creates a dictionary to store the words
#for loop iterates through file to populate the dictionary
#also creates variable that stores word frequency
word_counts = {}
for word in text:
    word_counts[word] = word_counts.get(word, 0) + 1

#sort the dictionary with sorted() function
sorted_words = sorted(word_counts.keys())

#prints the words in the new sorted list along with the frequency
for word in sorted_words:
    print(f"{word}: {word_counts[word]}")

