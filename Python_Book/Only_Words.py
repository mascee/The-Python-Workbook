# Excercise 117. Only the words
# This program reads a string from the user and returns only words.

#import re

def onlyWords(text):
    words = text.split()
    return [word for word in words if word.isalpha()]
    # return re.findall(r'\b[a-zA-Z]+\b', text)

def main():
    text = input("Please type something: ")
    print(onlyWords(text))

if __name__ == "__main__":
    main()


