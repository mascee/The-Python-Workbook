# Exercise 142. Unique Characters.
# Create a program that determines and displays the number of unique characters
# in a string entered by the user.
# Use a dictionary to solve this problem

s = input("Enter a string: ")

characters = {}
for ch in s:
    characters[ch] = True

print(f"There are {len(characters)} unique characters in {s}. ")

