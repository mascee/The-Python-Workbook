# This program reads positive integer from the user and computes prime factors of the integer.

number = int(input("Please eneter a positive integer greater then 1 and I will print prime factorization of it: "))

factor = 2
while factor <= number:
    if number % factor == 0:
        print(factor)
        number = number // factor
    else:
        factor = factor + 1