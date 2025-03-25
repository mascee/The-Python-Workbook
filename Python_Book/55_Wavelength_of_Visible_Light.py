# This program reads a wavelenth from the user and reports its color.

wavelength = int(input("Visible light is from 380 to 750 nanometers. Please enter the wavelength and I will tell you its color. "))

if wavelength >= 380 and wavelength < 450:
    color = "Violet"
elif wavelength >=450 and wavelength < 495:
    color = "Blue"
elif wavelength >= 495 and wavelength < 570:
    color = "Green"
elif wavelength >= 570 and wavelength < 590:
    color = "Yellow"
elif wavelength >= 590 and wavelength < 620:
    color = "Orange"
elif wavelength >= 620 and wavelength < 750:
    color = "Red"
else:
    color = ""

if color == "":
    print("This wavelenght is out of range of visible light. ")
else:
    print(f"{wavelength} nanometers is a {color} color. ")