# This program converts ordinal date to gregorian.
# It uses the convertion to calculate due date of the baby.

from Ordinal import ordinalDate


#Gestational period is 280 days
Gest_Period = 280

def gregorianDate(year, ordinal_date):
    leap = False
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        leap = True
    
    if leap:
        month_lengths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = 1
    for days_in_month in month_lengths:
        if ordinal_date <= days_in_month:
            date = ordinal_date
            return (year, month, date)
        else:
            ordinal_date -= days_in_month
            month += 1

    # If we get here, something went wrong
    return ("Error", "Invalid ordinal date")

def main():
    year = int(input("What is the year? "))
    month = int(input("What is the month? "))
    date = int(input("What is the date? "))

    start_ordinal = ordinalDate(year, month, date)
    due_ordinal = start_ordinal + Gest_Period

    while True:
        leap = (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)
        days_in_year = 366 if leap else 365

        if due_ordinal <= days_in_year:
            break
        else:
            due_ordinal -= days_in_year
            year += 1

    due_year, due_month, due_day = gregorianDate(year, due_ordinal)
    print(f"Due date: {due_month}/{due_day}/{due_year}")

main()