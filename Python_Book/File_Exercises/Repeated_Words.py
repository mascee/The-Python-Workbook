# Exercise 168. Repeaded words.
# Write a program that detects repeaded words in a text file.
# When repeated word is found, the program should display a message that contains the 
# line number and the repeated word.
# Ensure that the program correctly handles the case where the same word appears 
# at the end of the line and the begining of the followinf line.
# The name of the file should be provided as the only argument in the command line.

import sys

if len(sys.argv) != 2:
    print("Provide a file to review in the command line.")
    quit()

try:
    with open(sys.argv[1], "r") as inf:
        previous_word = None
        line_number = 0
        found_repeated = False 

        for line in inf:
            line_number += 1
            words = line.strip().lower().split()

            for word in words:
                if word == previous_word:
                    print(f"Repeated word '{word}' found on line {line_number}")
                    found_repeated = True
                previous_word = word

        if not found_repeated:
            print("No repeated words found.")

except IOError:
    print(f"Could not open {sys.argv[1]}. Please try again.")
    quit()


