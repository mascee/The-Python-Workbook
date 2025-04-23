# An integer, n, is said to be perfect when the sum of all proper divisors of n is equal to n.
# This program determines if a number is a perfect number.
from Proper_Divisors import properDivisor

def perfectNumber(number):
    sum = 0
    p_Divisors = properDivisor(number)

    for i in p_Divisors:
        sum += i

    if sum == number:
        return True
    else: 
        return False
    
def main():
    print("Perfect numbers from 1 to 10000 are: ")
    for number in range(1, 10001):
        if perfectNumber(number) == True:
            print(number)
        else: 
            number += 1

if __name__ == "__main__":
    main()