# The area of a triangle can be computed using the following formula:
# area = b * h / 2
# Where b is a lenght of the base of the triangle, and h is its height.
# Write a program that allows user to enter values for b and h.
# The program should then compute and display the area of a triangle with 
# base lenght b and height h.

b = float(input("Enter base of a triangle in cm: "))
h = float(input("Enter height of a triangle in cm: "))

area = b * h / 2

print(f"The area of a trangle with a base {b:.2f} cm and height {h:.2f} cm is {area} cm\u00B2.  ")