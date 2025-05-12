# Exercise 161. What's that element again?
# Write a program that reads a file containing information about chemical elements 
# and stores it in one appropriate data structure.
# Then the program should read and process input from the user.
# If the user enters an integer then the program should display the symbol and name of the element with 
# the number of protons entered.
# If the user enters a non-integer value then the program should display 
# the number of protons for the element with that name or symbol.
# The program should display an appropriate error message if no element exists for the 
# name, symbol or number of protons entered.
# Continue to read input from the user until a blank line is entered.

elements_file = "elements.txt"
elements = {}

# Step 1: Read and store element data
with open(elements_file, "r") as file:
    for line in file:
        atomic_number, symbol, name = line.strip().split(",")
        elements[int(atomic_number)] = {
            "symbol": symbol,
            "name": name
        }


# Step 2: Handle user input
while True:
    element = input("Please enter your element (Press Enter to quit): ").strip()
    if element == "":
        break

    if element.isdigit():
        num = int(element)
        if num in elements:
            print(f"{num}: {elements[num]['symbol']}, {elements[num]['name']}")
        else:
            print("No element with that atomic number.")
    else:
        # Normalize user input
        query = element.capitalize()
        found = False
        for num, data in elements.items():
            if data["symbol"].lower() == query.lower() or data["name"].lower() == query.lower():
                print(f"{data['name']} ({data['symbol']}) has atomic number {num}")
                found = True
                break
        if not found:
            print("No element with that name or symbol.")
