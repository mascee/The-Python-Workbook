# Create a program that determones how quickly an object is travvelling when it hits the ground.
# The user will enter the height from which the object is dropped in meters (m).
# Because the object is dropped its initial speed in 0 m/s. Assume that the acceleration
# due to gravity is 9.8 m/s^2. You can use the formula: Vf = $\sqrt{Vi^2 + 2ad}$
# to compute the final spedd Vf when the initial speed, Vi, acceleration a, and distance,d, are known.

import math

height = float(input("Please enter the height in meters: "))

V = math.sqrt(2*9.8*height)

time = height/V

print(f"It will take {time:.2f} seconds for an object to fall from {height:.2f} m height. ")