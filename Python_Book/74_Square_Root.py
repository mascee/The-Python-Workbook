# This program uses Newton's method to compute square root number

number = input("Please enter a number and I will calculate it's square root: ")

while number != "":
    try:
        number = float(number)  # Convert input to float
        if number < 0:
            print("This program works only for real numbers.")
        elif number == 0:
            print(f"The square root of {number} is 0.")
        else:
            guess = number / 2  # Initial guess
            while abs(guess * guess - number) > 10**-12:
                guess = (guess + number / guess) / 2 

            print(f"Square root of {number} is {guess:.2f}.")
            break
    except ValueError:
        print("Please enter a valid number.")
