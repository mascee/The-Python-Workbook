# This program creates a function that takes 3 integers as parameters.
# These parameters are a day, month and year.
# the function returns the day within the year for that date as its only result.

def ordinalDate(year, month, date):
    if month == 12:
        ordinal = date + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
    if month == 11:
        ordinal = date + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
    if month == 10:
        ordinal = date + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
    if month == 9:
        ordinal = date + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
    if month == 8:
        ordinal = date + 31 + 30 + 31 + 30 + 31 + 28 + 31
    if month == 7:
        ordinal = date + 30 + 31 + 30 + 31 + 28 + 31
    if month == 6:
        ordinal = date + 31 + 30 + 31 + 28 + 31
    if month == 5:
        ordinal = date + 30 + 31 + 28 + 31
    if month == 4:
        ordinal = date + 31 + 28 + 31
    if month == 3:
        ordinal = date + 28 + 31
    if month == 2:
        ordinal = date + 31
    elif month == 1:
        ordinal = date

    return ordinal

def main():
    year = int(input("What is the year? "))
    month = int(input("What is the month? "))
    date = int(input("What is the date? "))
    ordinal = ordinalDate(year, month, date)
    print(f"Ordinal date: {year}, {ordinal}. ")

main()
