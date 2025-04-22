# A magic date is a date where the day multiplied by the month is equal
# to the two digit year. For example, June 10, 1960 is a magic date.
# This program determines if a date is a magic date.
# Main function find all magic dates is 20th century

from Days_In_Month import days_in_month

def magicDates(day, month, year):
    if month * day == year % 100:
        return True
    return False

def main():
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, days_in_month(month, year) + 1):
                if magicDates(day, month, year):
                    print(f"{day}/{month}/{year} is a magic date. ")

main()

