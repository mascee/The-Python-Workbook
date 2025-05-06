# Exercise 154. Letter frequencies.
# This program reads a file from a command line and calculates how many times each letter occurs in the file.
# The program is case insensitive.

import sys
from collections import Counter


if len(sys.argv) != 2:
    print("Provide a file name as a command line argument. ")
    quit()

try:
    inf = open(sys.argv[1], "r")
    letter_counts = Counter()
    while True:
        char = inf.read(1)
        if not char:
            break
        if char.isalpha():
            char = char.lower()
            letter_counts[char] += 1

    for letter in sorted(letter_counts):
        print(f"{letter}: {letter_counts[letter]}")

except IOError as e:
    print("Error occurred while processing the file.")
    quit()