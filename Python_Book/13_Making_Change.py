#Program for self checkout
#Determine how much change to give
#How many coins to give
#Coins available: nickels, dimes, quarters, loonies, toonies.


import math

toonie = 200
loonie = 100
quarter = 25
dime = 10
nickel = 5

cents = int(input("Please enter how much cents do you have. "))
print(cents // toonie, "toonies")
cents = cents % toonie

print(cents // loonie, "loonies")
cents = cents % loonie

print(cents // quarter, "quaters")
cents = cents % quarter

print(cents // dime, "dimes")
cents = cents % dime

print(cents // nickel)
cents = cents % nickel