# This program finds next prime number

from Is_Number_Prime import is_prime

def nextPrime(n):
    if n < 2:
        return 2
    i = 1
    while not is_prime(n + i):
        i += 1
    return n + i

def main():
    n = int(input("Enter integer and I will tell you next prime number after it: "))
    result = nextPrime(n)
    print(f"Next prime number after {n} is {result}. ")
    

if __name__ == "__main__":
    main()
        
    
