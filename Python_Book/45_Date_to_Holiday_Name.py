# This program reads month and day from the user and matches it with 3 of canadian hoidays: NY, Christmas and Canada's Day.

month = input("Please enter month: ")
day = int(input("Please enter day: "))


if month == "January":
    if day == 1:
        print("It's a New Year! ")
    else:
        print("No holiday on this day. ")
elif month == "July":
    if day == 1:
        print("It's Canada's Day! ")
    else:
        print("No holiday on this day. ")
elif month == "December":
    if day == 25:
        print("It's Christmas Day! ")
    else:
        print("No holiday on this day. ")
else:
    print("No holiday on this day. ")

