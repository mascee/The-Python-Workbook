# Exercise 157. Both Letter Grades and Grade Points.
# Write a program that converts from letter grades to grade points and vice-versa.
# This program should allow the user to convert multiple values,
# with one value entered on each line.
# Begin by attempting to convert each value entered by the user from a number
# of grade points to a letter grade. If an exception occurs during this process
# then the program should attempt to convert the value from a letter grade to a number
# of grade points. If both conversions fail then the program should output a messgae indicating 
# that the supplied input is invalid. Design the program so that it continues performing 
# conversions ( or reporting errors) until the user enters a blank line.

grades = {
    "A+": "4.0",
    "A": "4.0",
    "A-": "3.7",
    "B+": "3.3",
    "B-": "3.0",
    "C+": "2.3",
    "C": "2.0",
    "C-": "1.7",
    "D+": "1.3",
    "D": "1.0",
    "F": "0.0"
}

total = 0
letter_grades = []
number_grades = []
count = 0

while True:
    user_input = input("Enter your grade (blank to exit): ").strip()
    if user_input == "":
        break

    try:
        # Try converting numeric grade to letter grade
        float_input = float(user_input)
        matched = False
        for letter, num in grades.items():
            if float(num) == float_input:
                print(f"{float_input} is equivalent to {letter}")
                total += float_input
                number_grades.append(float_input)
                letter_grades.append(letter)
                count += 1
                matched = True
                break
        if not matched:
            print("Grade point does not match any letter grade.")
    except ValueError:
        # Try converting letter grade to numeric grade
        upper_input = user_input.upper()
        if upper_input in grades:
            print(f"{upper_input} is equivalent to {grades[upper_input]}")
            num_value = float(grades[upper_input])
            total += num_value
            letter_grades.append(upper_input)
            number_grades.append(num_value)
            count += 1
        else:
            print("Invalid input.")

# Final output
if count > 0:
    GPA = total / count
    print(f"Your letter grades: {letter_grades}")
    print(f"Your number grades: {number_grades}")
    print(f"Your GPA: {GPA:.2f}")
else:
    print("No valid grades entered.")
