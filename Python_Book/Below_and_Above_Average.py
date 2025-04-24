# Excercise 119. Bellow and Above Average
# This program reads numbers from the user untill blank line is entered.
# Then the program displays an average of those numbers, all numbers bellow average, above average.

numbers = []
while True:
    user_input = input("Enter a number(press Enter to finish): ")
    if user_input == "":
        break
    try:
        numbers.append(float(user_input))
    except ValueError:
        print("Enter a valid number: ")

if numbers:
    avg = sum(numbers)/len(numbers)


print(f"Average is {avg}. ")
above_average = []
for number in numbers:
    if number > avg:
        above_average.append(number)
print(f"Above average numbers are: {above_average}. ")


below_average = []
for number in numbers:
    if number < avg:
        below_average.append(number)
print(f"Below average numbers are {below_average}")

