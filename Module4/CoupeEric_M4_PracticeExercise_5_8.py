"""

Author:  Eric Coupe
Date written: 11/16/2024
Assignment:   Module04 Practice Exercise 5-7
Short Desc:   A program that opens a text file with data and places the
              text in alphabetical order and shows the frequency the
              word occurs.
"""

with open("ConcordanceTest.txt", 'r') as file:
    text = file.read().split()

word_counts = {}
for word in text:
    word_counts[word] = word_counts.get(word, 0) + 1

sorted_words = sorted(word_counts.keys())

for word in sorted_words:
    print(f"{word}: {word_counts[word]}")

