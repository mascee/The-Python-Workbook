# A proper divisor is a positive integer, n, is a positive integer less then n which 
# divides evenly into n. 
# This program computes all of the proper divisors of a positive integer.
# The integer is passed to the funtion as its only parameter.

def properDivisor(number):
    p_divisors = []
    for i in range(1, number):
        if number % i == 0:
            p_divisors.append(i)

    return p_divisors

def main():
    number = int(input("Please enter an integer: "))
    p_divisors = properDivisor(number)
    print(f"Proper divisors of a number {number} are {p_divisors}")

if __name__ == "__main__":
    main()