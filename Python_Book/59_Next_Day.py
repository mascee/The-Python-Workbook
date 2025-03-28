# This program reads the date from the user and computes and displays the next day.

from datetime import datetime, timedelta

# Read date as a string
date = input("Please enter a date (YYYY-MM-DD): ")

try:
    # Convert to datetime object
    date_obj = datetime.strptime(date, "%Y-%m-%d")

    # Compute next day by adding 1 day
    next_day = date_obj + timedelta(days=1)

    print(f"You entered {date_obj.date()}. Next day is {next_day.date()}")

except ValueError:
    print("Invalid date format! Please use YYYY-MM-DD.")



