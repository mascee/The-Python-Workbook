# Exercise 158. Remove Commants.
# This program remove all comments from a file(# and all characters till the end of the line),
# and saves it to a new file.
# Both the name of the input file and the name of the output file should be
# read from the user.

try:
    input_file = input("Enter the name of the file to delete all comments: ")
    inf = open(input_file, "r")

except FileNotFoundError as e:
    print(f"{input_file} Not Found. ")
    quit()

try:
    output_file = input("Enter the output file: ")
    out = open(output_file, "w")
except FileNotFoundError as e:
    print(f"{output_file} Not Found. ")
    quit()

    


