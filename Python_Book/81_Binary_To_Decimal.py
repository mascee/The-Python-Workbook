# This program converts binary number to decimal

binary_number = input("Please enter a binary number: ")
decimal_number = 0

for i, digit in enumerate(binary_number[::-1]):
    decimal_number += int(digit) * (2**i)

print(f"Binary number {binary_number} is decimal: {decimal_number}. ")
