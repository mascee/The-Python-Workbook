# This program creates a function that takes 3 integers as parameters.
# These parameters are a day, month and year.
# the function returns the day within the year for that date as its only result.

def ordinalDate(year, month, date):

    January = 31
    March = 31
    April = 30
    May = 31
    June = 30 
    July = 31
    August = 31
    September = 30
    October = 31
    November = 30
    December = 31

    leap = False
    # Determine if leap year
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
    
    if leap == True:
        February = 29
    else:
        February = 28


    if month == 12:
        ordinal = date + November + October + September + August + July + June + May + April + March + February + January
    if month == 11:
        ordinal = date + October + September + August + July + June + May + April + March + February + January
    if month == 10:
        ordinal = date + September + August + July + June + May + April + March + February + January
    if month == 9:
        ordinal = date + August + July + June + May + April + March + February + January
    if month == 8:
        ordinal = date + July + June + May + April + March + February + January
    if month == 7:
        ordinal = date + June + May + April + March + February + January
    if month == 6:
        ordinal = date + May + April + March + February + January
    if month == 5:
        ordinal = date + April + March + February + January
    if month == 4:
        ordinal = date + March + February + January
    if month == 3:
        ordinal = date + February + January
    if month == 2:
        ordinal = date + January
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
