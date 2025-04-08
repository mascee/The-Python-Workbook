# This program reads letter grade and computes and displays number grade.

letter_grade = input("What is your grade(in letters)? ")

letter_grade = letter_grade.capitalize()

if letter_grade == "A+":
    number_grade = 4.0
    print(f"{letter_grade} is {number_grade}")
elif letter_grade == "A":
    number_grade = 4.0
    print(f"{letter_grade} is {number_grade}")
elif letter_grade == "A-":
    number_grade = 3.7
    print(f"{letter_grade} is {number_grade}")
elif letter_grade == "B+":
    number_grade = 3.3
    print(f"{letter_grade} is {number_grade}")
elif letter_grade == "B-":
    number_grade = 3.0
    print(f"{letter_grade} is {number_grade}")
elif letter_grade == "C+":
    number_grade = 2.3
    print(f"{letter_grade} is {number_grade}")
elif letter_grade == "C":
    number_grade = 2.0
    print(f"{letter_grade} is {number_grade}")
elif letter_grade == "C-":
    number_grade = 1.7
    print(f"{letter_grade} is {number_grade}")
elif letter_grade == "D+":
    number_grade = 1.3
    print(f"{letter_grade} is {number_grade}")
elif letter_grade == "D":
    number_grade = 1.0
    print(f"{letter_grade} is {number_grade}")
elif letter_grade == "F":
    number_grade = 0.0
    print(f"{letter_grade} is {number_grade}")
else: 
    print("Error. ")
