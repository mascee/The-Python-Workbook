# Creat a program that reads a duration from the user as a number of days, hours, minutes, and seconds.
# Compute total number of seconds.



days = int(input("Enter number of days: "))
hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
seconds = int(input("Enter number of seconds: "))

total_seconds = seconds + minutes * 60 + hours * 60 * 60 + days * 24 * 60 * 60 

print(f"Total number of seconds {total_seconds}: ")