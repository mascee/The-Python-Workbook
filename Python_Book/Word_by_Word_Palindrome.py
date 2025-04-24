# Excercise 118. Word by Word Palindrome.
# This program creates a function that determines if a string is a word by word palindrome.

from Only_Words import onlyWords

def word_by_word_palindrome(text):
    words= onlyWords(text.lower())

    return words == words[::-1]

    
def main():
    words = input("Please type some words: ")
    if word_by_word_palindrome(words):
        print("This is a word palindrome. ")
    else:
        print("This is not a word palindrome")

if __name__ == "__main__":
    main()