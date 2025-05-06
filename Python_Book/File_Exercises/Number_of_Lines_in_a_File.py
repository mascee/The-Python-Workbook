# Exercise 152. Number of lines in a file.
# Create a program that reads lines from a file adds line numbers to them,
# and then stores the numbered lines into a new file.
# The name of the input file will be read from the user, as will the name of the new file that the program will create.
# Each line in the output file should begin with the line number, followed by a colon and a space,
# followed by the line from the input file.

import sys

if len (sys.argv) != 2:
    print("Provide a file name as a command line argument. ")
    quit()

try:
    new_file = open("file_for_152.txt", "w")
    inf = open(sys.argv[1], "r")
    num = 1
    line = inf.readline()
    for line in inf:
        new_file.write(f"{num}: {line}")
        num += 1
    inf.close()
    new_file.close()

except IOError as e:
    print("Error occured while processing the file. ")
    quit()


