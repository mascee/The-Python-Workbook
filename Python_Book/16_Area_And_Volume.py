# Take radius from the user. Calculate the area and volume

radius = float(input("Please enter the radius of the circle in cm. "))

pi = 3.14

area = pi*radius ** 2
volume = 4/3*pi* (radius ** 3)

print(f"The area of a circle with a radius {radius} cm is {area:.2f} cm\u00B2. ")
print(f"The volume of a sphere with a radius {radius} cm is {volume:.2f} cm\u00B3. ")