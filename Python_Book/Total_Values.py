# Exercise 173. Total values. Recursion
# Write a program that reads values from the user until blank line is entered.
# Display the total of all the values entered by the user.

def total_values():
    line = input("Enter a number. Blank to quit: ")
    if line == "":
        return 0
    else:
        return float(line) + total_values()
def main():
    total = total_values()
    print(f"Total of all those values is {total}")

if __name__ == "__main__":
    main()