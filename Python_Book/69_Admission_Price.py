# This program calculates the price of admission based on age:
# Guests 2 years old or younger are free
# Children between 3 and 12 $14.00
# Seniors 65 and over $18.00
# General admission $23.00
# The program reads all ages in the group and and displays total cost.

price = 0
total = 0

ages_input = input("Please enter age of all people in your group separated by comma. Enter space to exit: ")
ages = ages_input.replace(" ", "").split(",")

for age_str in ages:
    try:
        age = int(age_str)
        if age <=2:
            price = 0
        elif age >= 65:
            price = 18
        elif age > 2 and age < 65:
            price = 23
        total += price
    except ValueError:
        print(f"Invalid input: {age_str} is not a number.")

print(f"Total admission cost: ${total:.2f}")

        





