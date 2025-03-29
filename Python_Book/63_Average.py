# This program countes average from the collection of numbers.
# The user ends the sequence of numbers by entering 0.
# If the first number is 0, the program displays error.

count = 0
sum = 0
number = 1

while number != 0:
    number = int(input("Please enter a number. Enter 0 to end sequence: "))
    count = count + 1
    sum = sum + number 

average = sum / count

print(f"Average is {average}. ")

