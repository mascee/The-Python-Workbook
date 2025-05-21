# Exercise 177. Roman Numerals.
# Create a recursive function that converts a Roman numeral to an integer.
# The function should process one or two characters at the begining of the string,
# then call itself recursively on all of the unprocessed characters.
# Use an empty string which has the value 0, for the base case.
# In addition, write a main program that reads a Roman numeral from the user and displays its value.
# You can assume that the value entered by the user is valid.

Roman_Numerals = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}

def Roman_to_Integer(roman_numeral):
    if roman_numeral == "":
        return 0
    elif len(roman_numeral) >= 2 and roman_numeral[:2] in Roman_Numerals:
        return Roman_Numerals[roman_numeral[:2]] + Roman_to_Integer(roman_numeral[2:])
    else:
        return Roman_Numerals[roman_numeral[0]] + Roman_to_Integer(roman_numeral[1:])

    
def main():
    roman_numeral = input("Enter a Roman Numeral and I will convert to integer: ").upper()
    integer = Roman_to_Integer(roman_numeral)
    print(f"{roman_numeral} is {integer}.  ")

if __name__ == "__main__":
    main()

