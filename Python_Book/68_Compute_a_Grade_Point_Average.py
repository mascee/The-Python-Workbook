# This program taks several letter grade inputs from the user, converts them to number grade
# and calculates the average grade.

letter_to_number = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0.0
}

letter_grade = input("Please enter your letter grades separated by space(Blank to quit): ").upper()
grades = letter_grade.split(" ")

total = 0
count = 0

for grade in grades:
    if grade in letter_to_number:
        total += letter_to_number[grade]
        count+=1
    else:
        print(f"Invalid grade {grade}")

if count > 0:
    avg = total/count
    print(f"Average grade is {avg:.2f}")
else:
    print("Error")
