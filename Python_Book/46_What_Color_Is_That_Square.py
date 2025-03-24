# This program takes chess position from the user and determines what color of a square this is.

letter = input("What is the letter of the chess position? ")
number = int(input("What is the number of the chess position? "))

letter_lower = letter.lower()


if letter_lower == "a" or letter_lower == "c" or letter_lower == "e" or letter_lower == "g":
    if number == 1 or number == 3 or number == 5 or number == 7:
        print(f"{letter}{number} is black. ")
    elif number == 2 or number == 4 or number == 6 or number == 8:
        print(f"{letter}{number} is white. ")
    else:
        print("Error. ")
elif letter_lower == "b" or letter_lower == "d" or letter_lower == "f" or letter_lower == "h":
        if number == 1 or number == 3 or number == 5 or number == 7:
            print(f"{letter}{number} is white. ")
        elif number == 2 or number == 4 or number == 6 or number == 8:
            print(f"{letter}{number} is black. ")
        else:
             print("Error. ")
else: 
     print("Error. ")


    