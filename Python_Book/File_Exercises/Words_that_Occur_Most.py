# Exercise 155. Words that Occur Most.
# This program determines words that occur most in the file

import sys
import string

word_counts = {}

if len(sys.argv) != 2:
    print("Provide a file name as a command line argument.")
    quit()

try:
    with open(sys.argv[1], "r") as inf:
        for line in inf:
            words = line.split()
            # Strip punctuation and make the words lowercase
            cleaned_words = [word.strip(string.punctuation).lower() for word in words]
            for word in cleaned_words:
                if word.isalpha():  # Only words with alphabetic characters
                    word_counts[word] = word_counts.get(word, 0) + 1

    if not word_counts:
        print("The file is empty or has no valid words.")
        quit()

    max_count = max(word_counts.values())
    most_popular = [word for word, count in word_counts.items() if count == max_count]
    print(f"Words that occur the most ({max_count} times): {', '.join(most_popular)}")

except IOError as e:
    print("Error occurred while processing the file.")
    quit()
