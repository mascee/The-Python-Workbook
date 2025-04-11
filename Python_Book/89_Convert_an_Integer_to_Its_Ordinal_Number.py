# Words like "first", "second", "third" are referred to as ordinal numbers.
# This program creates a function that converts numbers 1 to 12 to strings (ordinal numbers).
# It returns empty string when out of range.

int_to_ordinal = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve"
}

def ordinal(number):
    return int_to_ordinal.get(int(number), "")


def main():
    number = int(input("Enter a number from 1 to 12: "))
    converted_number = ordinal(number)
    print(f"{number} is {converted_number} ")

main()