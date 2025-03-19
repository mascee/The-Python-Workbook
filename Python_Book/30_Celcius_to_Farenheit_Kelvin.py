#Write a program that converts temperature from Celcius to Farenheit and Kelvin.

temp_C = float(input("Please enter temperature in Celcius: "))

temp_Kelvin = temp_C + 273.15

temp_Farenheit = (temp_C * 9 / 5) + 32

print(f"{temp_C:.1f} C is {temp_Kelvin:.1f} K and {temp_Farenheit:.1f} F. ")