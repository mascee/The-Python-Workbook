# This program reads words from the user and removes duplicates.

words = []
word = input("Please enter a word(black to quit): ")
while word != "":
    if word not in words:
        words.append(word)
    
    word = input("Please enter a word(black to quit): ")

for word in words:
    print(word)

