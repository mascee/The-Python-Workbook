# Exercise 154. Letter frequencies.
# This program reads a file from a command line and calculates how many times each letter occurs in the file.
# The program is case insensitive.

import sys

if len(sys.argv) != 2:
    print("Provide a file name as a command line argument. ")
    quit()

letter_count = {}

try:
    with open(sys.argv[1], "r") as inf:
        while True:
            char = inf.read(1)
            if not char:
                break
            char = char.lower()
            if char.isalpha():
                if char in letter_count:
                    letter_count[char] += 1
                else:
                    letter_count[char] = 1

    # Print in alphabetical order
    for letter in sorted(letter_count):
        print(f"{letter}: {letter_count[letter]}")
    inf.close()

except IOError as e:
    print("Error occurred while processing the file.")
    quit()