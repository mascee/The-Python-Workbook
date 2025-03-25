# This program reads wavelenght and classifies it

wave_lenght = float(input("Please enter any wavelenght: "))

if wave_lenght < 3 * 10**9:
    wave_name = "Radio Waves"
elif wave_lenght >= 3* 10**9 and wave_lenght < 3 * 10**12:
    wave_name = "Microwaves"
elif wave_lenght >= 3 * 10**12 and wave_lenght < 4.3 * 10**14:
    wave_name = "Infrared Light"
elif wave_lenght >= 4.3 * 10**14 and wave_lenght < 7.5 * 10**14:
    wave_name = "Visible Light"
elif wave_lenght >= 7.5 * 10**14 and wave_lenght < 3* 10**17:
    wave_name = "Ultraviolet Light"
elif wave_lenght >= 3 * 10**17 and wave_lenght < 3 * 10**19:
    wave_name = "X-Rays"
elif wave_lenght >= 3 * 10**19:
    wave_name = "Gamma Rays"
else:
    wave_name = ""

if wave_name == "":
    print("Invalid number")
else:
    print(f"{wave_lenght} Hz is in range of {wave_name}. ")
