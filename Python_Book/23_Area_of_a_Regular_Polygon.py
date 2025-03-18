# Compute area of a polygon

import math 

s = float(input("Enter lenght of the side of the polygon in cm: "))
n = int(input("How many sides in your polygon?: "))

area = (n * (s**2)) / (4 * math.tan(3.14 / n))

print(f" The area of the polygon with {n} sides with each side {s:.2f} cm is {area:.2f} cm\u00B2")