# Write a program that finds when is Easter each year.
# Use Anonymous Gregorian Computus algorithm

year = int(input("Enter a year and I will tell you what day is Easter on that year. "))

#Set a equal to the remainder when year is divided by 19
a = year % 19

#Set b equal to the floor of the year divided by 100
b = year // 100

#Set c equal to the remainder when year is divided by 100
c = year % 100

#Set d equal to the floor of b divided by 4
d = b // 4

#Set e equal to the remainder when b is divided by 4
e = b % 4

#Set f equal to the floor of (b+8)/25
f = (b + 8) // 25

#Set g equal to the floor of (b - f + 1) / 3
g = (b - f + 1) // 3

#Set h equal to the remainder when 19a + b - d - g +15 is divided by 30
h = (19 * a + b - d - g +15) % 30

#Set i equal to the floor of c divided by 4
i = c // 4

#Set k equal to the remainder when c is divided by 4
k = c % 4

#Set l equal to the remainder when 32+2e+2i-h-k is divided by 7
l = (32 + 2*e +2*i -h - k) % 7

#Set m equal to the floor of (a+11h+22l)/451
m = (a + 11*h +22*l) // 451

#Set month equal to the floor of (h+l-7m+114)/31
month = (h + l -7*m +114) // 31

#Set day equal to one plus the remainder when h+l-7m+114 is divided by 31.
day = 1 + ((h + l -7* m + 114) % 31)

print(f"On the year {year} the Easter is on {month}/{day}.")
