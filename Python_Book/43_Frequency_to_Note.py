# This program reads frequency and tells what music note this is.

frequency = float(input("Please enter frequency in Hz and I will tell you what music note this is: "))

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

closest_note = None
smallest_diff = float('inf')

for octave in range(1, 8):
    for note, base_freq in base_frequencies.items():
        # Adjust frequency for the current octave
        freq = base_freq / (2 ** (4 - octave))
        diff = abs(freq - frequency)
        if diff < smallest_diff:
            smallest_diff = diff
            closest_note = note
            closest_octave = octave

print(f"The closest note to {frequency} Hz is {closest_note}{closest_octave} ({round(freq, 2)} Hz).")
