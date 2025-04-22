# Excercise 106. Days in Month
# This program determines how many days in a particular month.
# The function takes 2 parameters: the month as an integer between 1 and 12 and a year as 4 digit integer.
# The program takes account of leap years too.


def days_in_month(month, year):
    leap = False
    days = 0

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        False

    if leap == True and month == 2:
        days = 29
    elif leap == False and month == 2:
        days = 28
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    else:
        print("Invalid date")

    return days

def main():
    month, year = map(int,input('Enter month as a number and year as 4 digits separated by space: ').split(" "))
    days = days_in_month(month, year)
    print(f"There are {days} days in the {month} month of the {year} year. ")


if __name__ == "__main__":
    main()

