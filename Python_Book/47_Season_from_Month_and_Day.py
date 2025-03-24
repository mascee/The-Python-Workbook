# This program takes month and day from the user and displays what season associated with the date.

month = input ("Please enter the month: ")
day = int(input("Please enter the day: "))

#Spring March 20
#Summer June 21
#Fall September 22
#Winter December 21

month = month.capitalize()

if month == "January" or month == "February":
    print("It's winter.")
elif month == "March" and day < 20:
    print("It's winter. ")
elif month == "March" and day >=20:
    print("It's Spring. ")
elif month == "April" or month == "May":
    print("It's Spring. ")
elif month == "June" and day < 21:
    print("It's Spring. ")
elif month == "June" and day >=21:
    print("It's Summer. ")
elif month == "July" or month == "August":
    print("It's Summer. ")
elif month == "September" and day < 22:
    print("It's Summer. ")
elif month == "September" and day >= 22:
    print("It's Fall. ")
elif month == "October" or month == "November":
    print("It's Fall. ")
elif month == "December" and day < 21:
    print("It's Fall. ")
elif month == "December" and day >= 21:
    print("It's Winter.")
else:
    print("Error. ")


