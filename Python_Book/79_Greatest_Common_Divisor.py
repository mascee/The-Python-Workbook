# This program reads two positive integers and finds common divisor

n, m = map(int, input("Enter two integers separated by space: ").split())

if n < m:
    d = n
    while m % d != 0:
        d = d -1
    print(f"The common divisor of {n} and {m} is {d}. ")    
elif m < n:
    d = m
    while n % d != 0:
        d = d -1
    print(f"The common divisor of {n} and {m} is {d}. ")
else:
    d = n
    print(f"Greatest common divisor of {n} and {m} is {n}. ")