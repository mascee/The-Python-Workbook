# Exercise 179. Recursive Square Root
# Create a square root function with two parameters. The first parameter n, 
# will be the number for which the square root is being computed.
# The second parameter, "guess", will be the current guess for the square root.
# The guess parameter should have default value of 1.0


def square_root(n, guess=1.0):
    if n == 0:
        return 0
    elif abs(guess**2 -n) < 1e-12:
        return guess
    else:
        new_guess = (guess + n/guess) / 2
        return square_root(n, new_guess)
    

def main():
    number = int(input("Enter any positive number and I will compute a square root: "))
    guess = 1
    sq_root = square_root(number, guess)
    print(f"Square root of {number} is {sq_root:.2f} ")

if __name__ =="__main__":
    main()

