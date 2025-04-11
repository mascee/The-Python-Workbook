# This program writes the finction that takes two sides of a right triangle 
# and computes a hypotenuse.

import math

def hypotenuse(side_1, side_2):
    hypotenuse = math.sqrt(side_1**2 + side_2**2)
    return hypotenuse

def main():
    side_1 = float(input("Enter one side of the right triangle(not a hypotenuse) in cm: "))
    side_2 = float(input("Enter the other side of the right triangle(not a hypotenuse) in cm: "))
    hyp = hypotenuse(side_1, side_2)
    print(f"Hypotenuse of a right triangle with sides {side_1:.2f} cm and {side_2:.2f} cm is {hyp:.2f} cm. ")

main()