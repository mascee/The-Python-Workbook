# Write a program to calculate wind chill.
# Wind chill is only valid for temperatures less then 10 C and wind speed > 4.8 km/h.

import math

temperature = float(input("Please enter temperature in C: "))
wind_speed = float(input("Please enter wind speed in km/h: "))

#Calculate wind chill:
WCI = 13.12 + 0.6215* temperature - 11.37 * (wind_speed**0.16) + 0.3965 * temperature * wind_speed**0.16

rounded_WCI = round(WCI)

print(f"The wind chill is {rounded_WCI}. ")