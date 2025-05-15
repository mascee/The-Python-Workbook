# Exercise 170. Missing Comments.
# This program reads a Python file, finds functtions without comments preceding them.

from sys import argv

if len(argv) != 2:
    print("Provide a Python file to review in the command line.")
    quit()

fname = argv[1]

try:
    with open(fname, "r") as inf:
        prev_line = ""
        line_number = 0

        for line in inf:
            line_number += 1
            stripped_line = line.lstrip()

            if stripped_line.startswith("def") and not prev_line.lstrip().startswith("#"):
                # Extract function name
                func_name = stripped_line[4:].split("(", 1)[0].strip()

                print(f"File: {fname} | Line: {line_number} | Missing comment before function: {func_name}")
            
            prev_line = line

except IOError:
    print(f"Could not open the file {fname}. Please try again.")
    quit()
