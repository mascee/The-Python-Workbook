# Exercise 151. Concatenate Multiple Files
# Unix based operating system typically include a tool named "cat",
# which is short for concatenate.
# Its purpose is to display the concatenation of one or more files
# whose names are provided as command line arguments.
# The files are displayed in the same order that they appear on the command line.
# This program performs this task.

import sys
#print(sys.argv)

if len(sys.argv) != 3:
    print("Please provide two files in the command line. ")
    quit()


try:
    inf = open(sys.argv[1], "r")   
    lines = []
    for line in inf:
        lines.append(line)
    inf.close()

    inf2 = open(sys.argv[2], "r")
    for line in inf2:
        lines.append(line)
    inf2.close()
except IOError as e:
    print("Error occured while processing the file. ")
    quit()

for line in lines:
    print(line, end = "")
    


