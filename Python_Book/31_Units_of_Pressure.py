# Create a program that reads a pressure from the user in kilopascals.
# Once the pressure has been read, program should report the equivelent pressure in pounds per square inch,
# millimeters of mercury and atmospheres.

# psi=kPa×0.145038
# mmHg=kPa×7.50062
# atm=kPa×0.00986923

kPa = float(input("Please enter pressure in Kilopascals: "))

psi = kPa * 0.145038
mmHg = kPa * 7.50062
atm = kPa * 0.00986923

print(f"{kPa:.2f} kPa is {psi:.2f} psi, {mmHg:.2f} mmHg, {atm:.2f} atm. ")

