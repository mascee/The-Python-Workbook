# Compute the area of a triangle is all sides are given

import math 

print("Please enter 3 sides of a triangle one by one: ")
s1 = float(input("Enter lenght of s1 in cm: "))
s2 = float(input("Enter lenght of s2 cm: "))
s3 = float(input("Enter lenght of s3 cm: "))

s = (s1 + s2 + s3) /2

area = math.sqrt(s*(s - s1) * (s - s2) * (s - s3))

print(f"Area of the triangle with sides {s1:.2f} cm, {s2:.2f} cm and {s3:.2f} is {s} cm\u00B2")