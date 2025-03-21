# This program reads a music note from the user and determines its frequency.

note = input("Please enter a music note in this format C4, D4, E4 etc: ")

#Notes frequencies

frequencies = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "B4": 493.88
}


if note in frequencies:
    {
        print(f"Frequency of a {note} is {frequencies[note]} Hz. ")
    }
else:
    {
        print("Note is not recognized. ")
    }
