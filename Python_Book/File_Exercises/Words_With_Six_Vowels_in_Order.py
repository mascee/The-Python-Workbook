# Exercise 172. Words with Six Vowels in Order.
# There is at least one word in the English language that contains each of the
# vowels A, E, I, O, U, Y exactly ones and in order. 
# Write a program that searches a file containing a list of words and displays all the words
# that meet this constraint. The user will provide the name of the file that will be searched.
# Display an appropriate error message and exit the program if the user provides an invalid file words
# with six vowels in order.

from sys import argv

if len(argv) != 2:
    print("Provide a Python file to review in the command line.")
    quit()
fname = argv[1]

# Define the required vowel sequence
vowel_seq = ['a', 'e', 'i', 'o', 'u', 'y']

def has_vowels_in_order(word):
    index = 0  # index in vowel_seq
    for ch in word:
        if index < len(vowel_seq) and ch == vowel_seq[index]:
            index += 1
    return index == len(vowel_seq)

try:
    with open(fname, "r") as inf:
        for line in inf:
            word = line.strip().lower()
            # Only consider words that contain all six vowels exactly once
            if all(word.count(v) == 1 for v in vowel_seq) and has_vowels_in_order(word):
                print(word)
except FileNotFoundError as e:
    print(f"Error: The file '{fname}' was not found.")