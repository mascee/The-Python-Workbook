# Exercise 171. Consistent Line Lengths.
# While 80 characters is a common width for a terminal window,
# some terminals are narrow or wider.
# This can present challenges when displaying documents containing paragraphs of text.
# The lines might be too long and wrap, making them difficult to read, or they might be too short
# and fail to make good use of the available space.
# Write a program that opens a file and displays it so that each line is as full as possible.
# If you read a line that is too long, then the program should break it up into words and add them to the current
# line until it is full. Then the program should start a new line and display the remaining words. If the line is too short, then 
# use words from the next line of the file to finish filling the current output.
# Ensure that the program works correctly for files containing multiple paragraphs of text.
# You can detect the end of one paragraph and the begining of the next by looking for lines that are 
# empty ones the end of the line marker has been removed.
# Hint: Use a constant to represent the maximum line length.

from sys import argv

if len(argv) != 2:
    print("Provide a Python file to review in the command line.")
    quit()

fname = argv[1]

LENGTH = 80

try:
    with open(fname, "r") as inf:
        words = []
        # Read the file and store all words, treating empty lines as paragraph breaks
        for line in inf:
            stripped_line = line.strip()
            if stripped_line == "":
                # Empty line indicates a paragraph break
                if words:
                    # Flush current paragraph
                    current_line = ""
                    for word in words:
                        if len(current_line) + len(word) + 1 <= LENGTH:
                            if current_line:
                                current_line += " "
                            current_line += word
                        else:
                            print(current_line)
                            current_line = word
                    if current_line:
                        print(current_line)
                    print()  # Blank line between paragraphs
                    words = []
            else:
                words.extend(stripped_line.split())

        # Handle remaining words after file ends
        if words:
            current_line = ""
            for word in words:
                if len(current_line) + len(word) + 1 <= LENGTH:
                    if current_line:
                        current_line += " "
                    current_line += word
                else:
                    print(current_line)
                    current_line = word
            if current_line:
                print(current_line)

except FileNotFoundError:
    print(f"File '{fname}' not found.")