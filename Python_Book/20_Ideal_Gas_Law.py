# The ideal gas law is a mathematical approximation of the behavior of gasses
# as pressure, volume, and temperature change.
# It is usually stated as: PV = nRT
# where P is the pressure in Pascals, V is the volume in liters, 
# n is the amount of substance in moles,
# R is the ideal gas constant, equal to 9.314 J/mol K, 
# and T is the temperature in degrees Kelvin.
# Write a program that computes the amount of gas in moles when the user supplies the pressure,
# volume and temperature. Test your program by determining the number of moles of gas in a SCUBA tank.
# A typical SCUBA tank holds 12 liters of gas at a pressure of 20 000 000 Pascals (3000 PSI). 
# Room temperature is approximately 20 degrees Celsius or 68 degrees Ferenheit.

pressure = float(input("Enter pressure in Pascals: "))
volume = float(input("Enter volume in liters: "))
temperature = float(input("Enter temperature in Celcius: "))

n = pressure * volume / (9.314 * (temperature + 273.15))

print(f"Number is moles is {n:.2f}. ")
