# The surface of the Earth is curved, and the distance between degrees of longitude varies 
# with latitude. As a result, finding the distance between 2 points on the surface
# of the Earth is more complicated then simply usig the Pythagorean theorem.
# Let (t1, g1) and (t2, g2) be the latitude and longitude of 2 points on Earth's surface.
# The distance between these points, following the surface of the Earth, in kilometers is:
# distance = 6371.01*arccos(sin(latitude_1)*sin(latitude_2) + cos(latitude_1)cos(latitude_2)*cos(longitude_1-longitude_2))
#6371.01 km is Earth's radius
#Create a program that allows the user to enter the latitude and longitude of two points 
# on the Earth in degrees. Dislpay the distance between 2 points.

import math


latitude_1 = float(input("What is the first latitude? "))
longitude_1 = float(input("What is the first longitude? "))

print(f"First coordinates: ({latitude_1}, {longitude_1})")


latitude_2 = float(input("What is the second latitude? "))
longitude_2 = float(input("What is the second longitude? "))
print(f"Scond coordinates: ({latitude_2}, {longitude_2})")

latitude_1_radians = math.radians(latitude_1)
longitude_1_radians = math.radians(longitude_1)
latitude_2_radians = math.radians(latitude_2)
longitude_2_radians = math.radians(longitude_2)

print(f"Converted coordinates: (lt1, lg1) = ({latitude_1_radians}, {longitude_1_radians}). (lt2, lg2) = ({latitude_2_radians}, {longitude_2_radians})")


distance = 6371.01*math.acos(math.sin(latitude_1_radians)*math.sin(latitude_2_radians) + math.cos(latitude_1_radians)*math.cos(latitude_2_radians)*math.cos(longitude_1_radians-longitude_2_radians))

print(f"Distance between 2 points is {distance:.2f} km. ")