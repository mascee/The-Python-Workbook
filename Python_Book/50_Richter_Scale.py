# The program reads earthquake magnitude and add description as a part of meaningful message about the earthquake.

magnitude = float(input("Please enter the earthquake's magnitude: "))

if magnitude >= 0 and magnitude < 2:
    descriptor = "Micro"
elif magnitude >= 2 and magnitude < 3:
    descriptor = "Very Minor"
elif magnitude >= 3 and magnitude < 4:
    descriptor = "Minor"
elif magnitude >= 4 and magnitude < 5:
    descriptor = "Light"
elif magnitude >=5 and magnitude < 6:
    descriptor = "Moderate"
elif magnitude >=6 and magnitude < 7:
    descriptor = "Strong"
elif magnitude >=7 and magnitude < 8:
    descriptor = "Major"
elif magnitude >=8 and magnitude < 9:
    descriptor = "Great"
elif magnitude >= 9 and magnitude < 10:
    descriptor = "Meteoric"
elif magnitude < 0:
    Exception("Please enter positive value. ")
else:
    Exception("Number is not defined. ")


print(f"The earthquake with a magnitude {magnitude} on Richter Scale is {descriptor}. ")