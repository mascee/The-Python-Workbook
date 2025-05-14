# Exercise 167. Spell Checker
# This program takes user input and shows words that were misspelled.
# The spell checking is performed by comparing the input with the list of English words from WordList.txt
# User enters a file as a command line argument to check for spelling mistakes.

import sys

if len(sys.argv) != 2:
    print("Please provide a file to review in the command line: ")
    quit()

try:
    inf = open(sys.argv[1], "r")   
except IOError as e:
    print(f"Error occured while processing the file {sys.argv[1]}. ")
    quit()


def onlyWords(text):
    words = text.split()
    return [word for word in words if word.isalpha()]

valid = {}
with open("WordList.txt", "r") as word_file:
    for word in word_file:
        word = word.lower().strip()
        #Add the word to dictionary
        valid[word] = 0

# Read each line from the file, adding any misspelled words to the list of misspelling
misspelled = []
for line in inf:
    words = onlyWords(line)
    for word in words:
        if word.lower() not in valid and word not in misspelled:
            misspelled.append(word)
inf.close()

if len(misspelled) == 0:
    print("No misspelled words. ")
else:
    print("The following words are misspelled: ")
    for word in misspelled:
        print(" ", word)