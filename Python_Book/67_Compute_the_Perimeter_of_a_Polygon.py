# This program computes perimeter of a polygon based on coordinates
import math

# List to store coordinates as tuples (x, y)
coordinates = []

# Read the first point
x = input("Enter the first x-coordinate of a polygon: ")
y = input("Enter the first y-coordinate of a polygon: ")

if x and y:
    coordinates.append((float(x), float(y)))
else:
    print("First coordinates are empty. Exiting.")
    exit()

# Read subsequent points
while True:
    x_next = input("Enter the next x-coordinate (blank to exit): ")
    y_next = input("Enter the next y-coordinate (blank to exit): ")

    if not x_next or not y_next:
        break  # Exit if either input is blank

    coordinates.append((float(x_next), float(y_next)))

# Calculate the perimeter
perimeter = 0
for i in range(len(coordinates) - 1):
    x1, y1 = coordinates[i]
    x2, y2 = coordinates[i + 1]
    perimeter += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Close the polygon by adding the distance from last point to first
if len(coordinates) > 2:
    x1, y1 = coordinates[-1]
    x2, y2 = coordinates[0]
    perimeter += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"Perimeter is {perimeter:.2f}")