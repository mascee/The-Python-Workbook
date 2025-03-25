# This program reads letter grade and computes and displays number grade.

letter_grade = input("What is your grade(in letters)? ")

letter_grade = letter_grade.capitalize()

if letter_grade == "A+":
    print(f"{letter_grade} is 4.0")
elif letter_grade == "A":
    print(f"{letter_grade} is 4.0")
elif letter_grade == "A-":
    print(f"{letter_grade} is 3.7")
elif letter_grade == "B+":
    print(f"{letter_grade} is 3.3")
elif letter_grade == "B-":
    print(f"{letter_grade} is 3.0")
elif letter_grade == "C+":
    print(f"{letter_grade} is 2.3")
elif letter_grade == "C":
    print(f"{letter_grade} is 2.0")
elif letter_grade == "C-":
    print(f"{letter_grade} is 1.7")
elif letter_grade == "D+":
    print(f"{letter_grade} is 1.3")
elif letter_grade == "D":
    print(f"{letter_grade} is 1.0")
elif letter_grade == "F":
    print(f"{letter_grade} is 0.0")
else: 
    print("Error. ")
