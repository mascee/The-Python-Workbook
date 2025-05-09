# Exercise 159. Two Word Random Password
# Write a program that reads a file containing a list of words,
# randomly selects two of them, and concatinates them to produce a new password.
# Each word should be at least 3 letters long.
# Passowrd should be between 8 and 10 characters.
# Capitalize each word in the password, so the user can easily see where one word ends
# and the next one begins.
# The program should display the password.

from random import randrange

words = []

word_file = "test4.txt"

with open(word_file, "r") as inf:
    for line in inf:
        word = line.strip() #Removes trailing newline and spaces
        if len(word) >= 3:
            words.append(word)


while True:
     first = words[randrange(len(words))].capitalize()
     second = words[randrange(len(words))].capitalize()
     password = first + second
     if 8 <= len(password) <= 10:
         break
     
print(f"The password is: {password}")





