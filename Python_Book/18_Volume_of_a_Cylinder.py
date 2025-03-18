# The volume of a cylinder can be computed by multiplying the area
# of its circular base by its height. Write a program that reads the radius 
# of the cylinder, along with its height, from the user and computes its volume.
# Display the result rounder to one decimal place.

radius = float(input("What is the radius of the cylinder base in cm? "))
height = float(input("What is the height of the cylinder in cm? "))

volume = (3.14 * radius**2) * height

print(f"The volume of the cylinder with radius {radius:.1f} cm and height {height:.1f} cm is {volume:.1f}cm\u00B3. ")