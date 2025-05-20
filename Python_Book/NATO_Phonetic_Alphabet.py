# Exercise 176. The NATO Phonetic Alphabet
# Write a program that reads a word from the user and then displays its phonetic spelling.
# For example, if the user enters "Hello", 
# then the pregram should output Hotel Echo Lima Oscar
# The program should use recursive function. Do not use loop anywhere in the solution.
# Any non-letter characters should be ignored.

NATO_Alphabeth = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliet",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Wiskey",
    "X": "Xray",
    "Y": "Yankee",
    "Z": "Zulu"
}


def NATO_phonetic(message):
    if message == "":
        return []
    ch = message[0].upper()
    if ch in NATO_Alphabeth:
        return [NATO_Alphabeth[ch]] + NATO_phonetic(message[1:])
    else:
        # Skip non-letter character
        return NATO_phonetic(message[1:])

def main():
    word = input("Enter your message: ")
    result = NATO_phonetic(word)
    print(" ".join(result))

if __name__ == "__main__":
    main()