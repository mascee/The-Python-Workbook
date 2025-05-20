# Fibonacci numbers, using recursion
# The Fibonacci numbers are a sequence of integers that begin
# with 0 and 1. Each sunsequent number in the sequence is the sum of its
# two immediate predecessors.
# As a result, the first 10 numbers in the Fibonacci sequence are:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 

def fib(n):
    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    #Recursive case:
    return fib(n - 2) + fib(n - 2)

n = int(input("Enter a positive integer: "))
print(fib(n))