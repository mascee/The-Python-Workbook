# This program reads a, b, c from the user and calculates number of of roots in quadratic formula
import math

a, b, c = map(int, input("Please enter numbers for a, b, and c separated by space: ").split())

discriminant = b ** 2 - 4 * a * c

if discriminant == 0:
    root_number = 1
    root = (-b) / (2 * a)
    print(f"This equation has {root_number} real root and it's {root}. ")
elif discriminant < 0:
    print("The equation doesn't have real roots. ")
elif discriminant > 0:
    root_number = 2
    root1 = (-b - math.sqrt(discriminant))/(2*a)
    root2 = (-b + math.sqrt(discriminant))/(2*a)
    print(f"This equation has {root_number} real roots and it's {root1} and {root2}. ")