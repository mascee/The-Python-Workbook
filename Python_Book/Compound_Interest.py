#Pretend that you have just opened a new savings account that earns 4 percent interest per year.
# The interest that you earn is paid at the end of the year, and is added to the balance
# of the savings account. Write program that begins by reading the amount of money 
# deposited into the account from the user.
#Then your program should compute and display the amount in the savings account after 1, 2, and 3 years.
# Display each amount so that it is rounded to 2 decimal places.

import math

balance = 0
deposit = int (input("Enter the deposited amount: "))
balance = (balance + deposit)

one_year_savings = balance + balance*0.04
two_year_savings = one_year_savings + one_year_savings*0.04
three_year_savings = two_year_savings + two_year_savings*0.04

print(f"One year saving: ${one_year_savings:.2f}.")
print(f"Two year savings: ${two_year_savings:.2f}.")
print(f"Three year savings: ${three_year_savings:.2f}.")
