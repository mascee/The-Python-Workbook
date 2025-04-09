# This program says "Fizz" if a number is divisible by 3
# "Buzz" if a number is divisible by 5
# And "Fizz Buzz" if divisible by both 3 and 5.
# The numbers are from 1 to 100


for number in range(1, 101, 1):

    if number % 3 == 0 and number % 5 == 0:
        print(f"{number}: Fizz Buzz")
    elif number % 5 == 0:
        print(f"{number}: Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print(f"{number}: Fizz")
