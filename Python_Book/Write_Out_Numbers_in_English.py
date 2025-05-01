# Exercise 141. Write numbers in English
# This program creates a function that takes an integer between 0 and 999
# as its only parameter, and returns a string containing the English words
# for that number.
# Use one or more dictionaries to implement it.

# Dictionaries
units = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
}

teens = {
    10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
    15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
}

tens = {
    20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
    60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
}


def number_to_words(number):
    if number == 0:
        return "Zero"
    
    words = []

    # Handle hundreds
    if number >= 100:
        hundreds_digit = number // 100
        words.append(units[hundreds_digit])
        words.append("Hundred")
        number %= 100  # get the remaining two digits

    # Handle 10–19
    if 10 <= number <= 19:
        words.append(teens[number])
    else:
        # Handle tens (20, 30, ..., 90)
        tens_digit = (number // 10) * 10
        units_digit = number % 10

        if tens_digit:
            words.append(tens.get(tens_digit, ""))  # get "" if not found
        if units_digit:
            words.append(units.get(units_digit, ""))

    return " ".join(words)

def main():
    number = int(input("Enter any number from 0 to 999: "))
    print(number_to_words(number))

if __name__ == "__main__":
    main()
