# This program reads year from the user and reports what day of the week is January 1 on that year.

year = int(input("Please enter the year: "))

#This formula is used to determine what day of the week is January 1. Sunday is 0
day_of_the_week = (year + (year -1 )//4 - (year - 1) // 100 + (year - 1) // 400) % 7

if day_of_the_week == 0:
    print(f"For the year {year} January 1st is Sunday.")
elif day_of_the_week == 1:
    print(f"For the year {year} January 1st is Monday.")
elif day_of_the_week == 2:
    print(f"For the year {year} January 1st is Tuesday.")
elif day_of_the_week == 3:
    print(f"For the year {year} January 1st is Wednesday.")
elif day_of_the_week == 4:
    print(f"For the year {year} January 1st is Thursday.")
elif day_of_the_week == 5:
    print(f"For the year {year} January 1st is Friday.")
elif day_of_the_week == 6:
    print(f"For the year {year} January 1st is Saturday.")
else: print("Error")








