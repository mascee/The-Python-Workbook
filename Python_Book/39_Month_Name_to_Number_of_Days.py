# This programs reads a month from a user and returns how many days in this month.

month = input("What month is it? ")

if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month =="December" :
    {
        print (f"{month} has 31 days.")
    }
elif month == "February":
    {
        print (f"{month} has 28 or 29 days. ")
    }
elif month == "April" or month == "June" or month == "September" or month == "November":
    {
        print (f"{month} has 30 days. ")
    }
else:
    {
        print("This is not a month. ")
    }