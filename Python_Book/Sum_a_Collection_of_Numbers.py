# Exercise 156. Sum a Collection of Numbers
# Create a program that sums all of the numbers entered by the user while ignoring any input 
# that is not a valid number.
# This program should display the current sum after each number is entered.
# It should display an appropriate message after each non-numeric input, and then continue
# to sum any additional numbers entered by the user. Exit the program when the user enters
# a blank line.
# Ensure that the program works correctly for both integers and floating-point numbers.
# This program uses exceptions.
import re

try:
    number_collection = []
    total = 0.0 

    while True:
        user_input = input("Please enter any number (or press Enter to stop): ")
        if user_input == "":
            break 

        number_pattern = r'-?\d+(?:\.\d+)?'
        found_numbers = re.findall(number_pattern, user_input)

        # Convert each number string to float and add to collection and total
        for num_str in found_numbers:
            num = float(num_str)
            number_collection.append(num)
            total += num

    print(f"Sum of numbers in {number_collection} is {total:.2f}")

except Exception as e:
    print("Not a valid input.")
    quit()
