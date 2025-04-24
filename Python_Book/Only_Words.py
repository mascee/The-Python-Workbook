# Excercise 117. Only the words
# This program reads a string from the user and returns only words.

#using regex
import re

def onlyWords(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    return ','.join(words)

def main():
    text = input("Please type something: ")
    print(onlyWords(text))

if __name__ == "__main__":
    main()


