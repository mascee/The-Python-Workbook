# This program reads integer from the user and determines if the inteher even or odd.

number = int(input("Please enter integer: "))

if number % 2 == 0 & number != 0:
    print(f"{number} is even. ")
elif number == 0:
    print(f"{number} is 0. ")
else:
    print(f"{number} is odd. ")