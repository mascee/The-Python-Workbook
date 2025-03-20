# This program reads letter from the user and tells if it's a vowel or consonant.

letter = input("Please enter any letter of the English Alphabet: ")
letter_lower = letter.lower()

if letter_lower == 'a' or letter_lower == 'e' or letter_lower == 'i' or letter_lower == 'o' or letter_lower == 'u':
    {
        print(f"Letter {letter_lower} is a vowel. ")
    }
elif not letter.isalpha():
    {
        print("This is not a letter from English Alphabeth. ")
    }
else:
    {
        print(f"Letter {letter_lower} is a consonant. ")
    }