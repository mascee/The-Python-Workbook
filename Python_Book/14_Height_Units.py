# Program that converts feet and inches to cm

feet, inches = map(int, input("Please enter feet and inches separated by space: ").split())


#Convert to cm
total_inches = feet*12 + inches
total_cm = total_inches*2.54

print(f"You entered {feet} feet, {inches} inches. This converts to {total_cm} cm. ")