# This program reads a music note from the user and determines its frequency.

note = input("Please enter a music note (C4, D4, E4, etc.): ")

# Notes base frequencies for the 4th octave
base_frequencies = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88
}

pitch = note[0]       # Get the note
octave = int(note[1]) # Get the octave number 

if pitch in base_frequencies:
    freq = base_frequencies[pitch] / (2 ** (4 - octave))  # Adjust frequency based on octave
    print(f"Frequency of {note} is {freq:.2f} Hz.")
else:
    print("Note is not recognized.")
