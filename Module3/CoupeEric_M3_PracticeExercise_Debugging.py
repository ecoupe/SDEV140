"""
Author:  Eric Coupe
Date written: 11/8/2024
Assignment:   Module03 Practice Exercise Debugging
Short Desc:   A program to analyze a text file and give it a Flesch
              score, sentence count, word count, and syllable count.
              Uses a nested for loop to iterate over each character
              in a word to find vowels and count syllables. 

"""

# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

# Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')

# Count the words
words = len(text.split())

# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    #added 'i' as an index variable to loop through each character
    #added 'prev_vowel' as a boolean flag for consecutive vowels
    i = 0
    prev_vowel = False
    #while loop iterates over each character in a word until it finds
    # a vowel. the syllable count increases by 1 and boolean flag set
    # to True. otherwise 'i' increases and iterates until the next
    # vowel is found 
    while i < len(word):
        if word[i] in vowels:
            if not prev_vowel:
                syllables += 1
                prev_vowel = True
            i += 1  # Skip over consecutive vowels
        else:
            prev_vowel = False
            i += 1
    for ending in ['es', 'ed', 'e']:
        # added additional logic gates to manage endings
        if word.endswith(ending) and len(word) > 2:
            syllables -= 1
    if word.endswith('le') and len(word) > 2:
        syllables += 1

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * \
                  (syllables / words) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")
