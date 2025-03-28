# This program simulates a Roulette Game

from random import randrange

roulette_number = randrange(0, 38)

if roulette_number == 37:
    print("Pay 00")
else:
    print(f"Pay {roulette_number}. ")

if (roulette_number >= 1 and roulette_number <= 9 and roulette_number % 2 == 1) or \
   (roulette_number >= 12 and roulette_number <= 16 and roulette_number % 2 == 0) or \
   (roulette_number >= 19 and roulette_number <= 27 and roulette_number % 2 == 1) or \
   (roulette_number >= 30 and roulette_number <= 36 and roulette_number % 2 == 0):
    print("Pay Red")

# Zero and 00 are neither red nor black
elif roulette_number == 0 or roulette_number == 37:
    pass
else:
    print("Pay Black")

# Odd/Even determination for numbers 1-36
if roulette_number >= 1 and roulette_number <= 36:
    if roulette_number % 2 == 1:
        print("Pay Odds")
    else:
        print("Pay Even")

# Low/High number ranges
if roulette_number >= 1 and roulette_number <= 18:
    print("Pay 1 to 18")
elif roulette_number >= 19 and roulette_number <= 36:
    print("Pay 19 to 36")