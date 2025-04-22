# Excercise 107
# Reduce a Fraction to Lowest Terms
# Write a function that takes 2 positive integers that represent the numerator and denominator
# of a fraction as its only parameters.
# The body of a function should reduce the fraction to lowest terms and return reduced numerator and denominator

def reduce_fraction(n, m):
    #Find common divisor
    if n < m:
        d = n
        while m % d != 0:
            d = d -1
    elif m < n:
        d = m
        while n % d != 0:
            d = d -1
    else:
        d = n

    reduced_numerator = n // d
    reduced_denominator = m // d
    return (reduced_numerator, reduced_denominator)

def main():
    n,m = map(int, input("Enter numberator and denominator separated by '/':  ").split('/'))
    reduced_n, reduced_den = reduce_fraction(n, m)
    print(f"Fraction {n}/{m} could be reduced to {reduced_n}/{reduced_den}.  ")

if __name__ == "__main__":
    main()