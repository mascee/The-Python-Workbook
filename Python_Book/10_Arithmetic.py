#Program reads 2 integers a and b from the user and displays: 
#The sum of a and b
#The product of a and b
#The quotient when a is divided by b
#The remainder when a is divided by b
#The result of log10 a
#The result of a to the power of b

import math

a = int(input("Please enter first integer: "))
b = int(input("Please enter second integer: "))

sum = a + b 
print(f"The sum of {a} and {b} is {sum}. ")

product = math.prod([a, b])
print(f"The product of {a} and {b} is {product}")

quotient, remainder = divmod(a, b)
print(f"Quotient of {a} and {b} is {quotient}. Remainder is {remainder}.  ")

log = math.log10(a)
print(f"Logarith of {a} base 10 is {log}. ")

power = math.pow(a, b)
print(f"The result of {a} to the power of {b} is {power}. ")