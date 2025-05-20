# This is an example of how recursive function works.
# The function adds up numbers.

def sum(n):
    if n <= 0:
        return 0
    else:
        return n + sum(n - 1)
    
number = int(input("Enter positive integer and I will tell the sum of all emements: "))
total = sum(number)
print(f"Sum of all elements up to {number} is: {total}")
