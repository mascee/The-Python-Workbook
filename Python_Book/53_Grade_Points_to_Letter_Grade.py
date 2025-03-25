# This program reads grades in numbers and converts to grade letters.

# Read grade points
gp = float(input("What is your grade in numbers? "))

if gp >= 4.0:
    letter = "A+"
elif gp == 3.7:
    letter = "A-"
elif gp == 3.3:
    letter = "B+"
elif gp == 3.0:
    letter = "B"
elif gp == 2.7:
    letter = "B-"
elif gp == 2.3:
    letter = "C+"
elif gp == 2.0:
    letter = "C"
elif gp == 1.7:
    letter = "C-"
elif gp == 1.3:
    letter = "D+"
elif gp == 1.0:
    letter = "D"
elif gp == 0:
    letter = "F"
else:
    letter = "Error"

if letter == "Error":
    print("Invalid number. " )
else:
    print(f"{gp} is {letter}. ")