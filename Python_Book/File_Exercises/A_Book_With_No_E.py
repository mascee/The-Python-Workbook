# Exercise 162.
# This program reads a list of words from a file and determines
# what proportion of the words use each letter of the alphabets.
# Display the result for all 26 letters and include additionas message
# that identifies the letter that is used in the smallest proportion of the word.

# Lipogram is a written work that does not use a particular letter.
# Find if the text is a lipogram

import string

file = "book.txt"
letter_counts = {letter: 0 for letter in string.ascii_lowercase}
total_words = 0

with open(file, "r") as book:
    for line in book:
        for word in line.strip().lower().split():
            cleaned = ''.join(filter(str.isalpha, word))  # Remove punctuation
            if cleaned:
                total_words += 1
                unique_letters = set(cleaned)
                for letter in unique_letters:
                    if letter in letter_counts:
                        letter_counts[letter] += 1
min_letter = None
min_proportion = 1

print("Proportion of words using each letter: ")
for letter in string.ascii_lowercase:
    proportion = letter_counts[letter] /total_words
    print(f"{letter}: {proportion:.2f}")
    if proportion < min_proportion:
        min_proportion = proportion
        min_letter = letter

print(f"\nLetter used in the smallest proportion of words: '{min_letter}' ({min_proportion:.2%})")