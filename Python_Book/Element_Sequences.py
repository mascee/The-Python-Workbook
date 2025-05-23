# Exercise 183. Element Sequences.
# Write a program that reads the name of an element from the user and uses a recursive function to find
# the longest sequence of elements that begin with that value.
# Display the sequence once it has been computed.
# Each element in the sequence begins with the last letter of its predecessor.

def longest_sequence(start, words):
    if start == "":
        return []

    longest = []
    last_letter = start[-1].lower()
    for i in range(len(words)):
        first_letter = words[i][0].lower()
        if first_letter == last_letter:
            candidate = longest_sequence(words[i], words[:i] + words[i + 1:])
            if len(candidate) > len(longest):
                longest = candidate
    return [start] + longest

def load_names():
    names = []
    with open("Data/Chemical_Elements.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) >= 3:
                names.append(parts[2])
    return names

def main():
    names = load_names()
    lower_to_original = {name.lower(): name for name in names}

    start_input = input("Enter the chemical element name: ").strip().lower()

    if start_input in lower_to_original:
        start = lower_to_original[start_input]
        names.remove(start)

        sequence = longest_sequence(start, names)

        print(f"A longest sequence that starts with {start} is:")
        for element in sequence:
            print(element)
    else:
        print("Sorry, that wasn't a valid element name.")

if __name__ == "__main__":
    main()
