# Read seconds from the user and convert them to D:HH:MM:SS
seconds = int(input("Enter number of seconds: "))

# One day is 86400 seconds.  24 * 60 * 60
SECONDS_IN_DAY = 86400 
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

days = seconds // SECONDS_IN_DAY
remaining_seconds  = seconds % SECONDS_IN_DAY

hours = remaining_seconds // SECONDS_IN_HOUR
remaining_seconds = remaining_seconds % SECONDS_IN_HOUR

minutes = remaining_seconds // SECONDS_IN_MINUTE
remaining_seconds = remaining_seconds % SECONDS_IN_MINUTE

print(f"{seconds} seconds is {days}:{hours:02}:{minutes:02}:{remaining_seconds:02}.")