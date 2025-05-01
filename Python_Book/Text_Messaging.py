# Exercise 138. Text Messaging
# On some basic cell phones text messages can be sent using the numeric keypad.
# Because each key has letters associated with it, multiple key presses are needed for most letters.
# Pressing the number ones generates the first character listed for that key.
# Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth character.
# This program displays the key presses needed for a message entered by the user.
# Example: For "HELLO, WORLD!" the program should output 4433555555666110966677755531111
from Reverse_Lookup import reverseLookup

key_symbols = {
    1: [".", ",", "?", "!", ":"],
    2: ["A", "B", "C"],
    3: ["D", "E", "F"],
    4: ["G", "H", "I"],
    5: ["J", "K", "L"],
    6: ["M", "N", "O"],
    7: ["P", "Q", "R", "S"],
    8: ["T", "U", "V"],
    9: ["W", "X", "Y", "Z"],
    0: [" "]
}

# Build a lookup dictionary: character -> keypress sequence
char_to_keypress = {}
for key, chars in key_symbols.items():
    for i, char in enumerate(chars):
        char_to_keypress[char.upper()] = str(key) * (i + 1)

# Get message input and convert it
message = input("Type your message: ").upper()

keypress_sequence = ""
for ch in message:
    if ch in char_to_keypress:
        keypress_sequence += char_to_keypress[ch]
    else:
        print(f"Skipping unsupported character: {ch}")

print("Key presses needed:", keypress_sequence)


