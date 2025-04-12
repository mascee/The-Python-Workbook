# Words like "first", "second", "third" are referred to as ordinal numbers.
# This program creates a function that converts numbers 1 to 12 to strings (ordinal numbers).
# It returns empty string when out of range.

int_to_ordinal = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
}

def ordinal(number):
    return int_to_ordinal.get(int(number), "")


def main():
    number = int(input("Enter a number from 1 to 12: "))
    converted_number = ordinal(number)
    print(f"{number} is {converted_number} ")

main()