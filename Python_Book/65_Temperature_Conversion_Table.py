# This program creates table of temperature conversion from Celcius to Farenheit
# From 0 to 100 C that are multiples of 10 degrees Celsius.

print("Table of Temperature Conversion from C to F:")

print(f"{'C':<10}{'F':<10}")

print("="*20)

for C in range(0, 101, 10):
    F = (C * 9/5) + 32
    print(f"{C:<10}{F:<10}")