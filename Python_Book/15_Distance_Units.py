# Takes input in feet from the user. 
# Converts to inches, yards, miles.

feet = float(input("Please enter distance in feet: "))

inches = feet*12
yards = feet/3
miles = feet*0.000189394

print(f"You entered {feet:.2f} feet. This is {inches:.2f} inches, {yards:.2f} yards, {miles:.6f} miles.")