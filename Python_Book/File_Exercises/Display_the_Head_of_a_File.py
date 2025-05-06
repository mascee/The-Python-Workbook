# Unix based operating system usually include a tool named head.
# It displays the first 10 lines of a file whose name is provided as a command
# line argument. Write a Python program that provides the same behaviour.
# Display an appropriate error message if the file requested by the user does not exist, 
# or if the command line argument is ommitted.

import sys
print(sys.argv)
NUM_LINES = 10

if len(sys.argv) != 2:
    print("Provide file name as a command line argument: ")
    quit()

try:
    inf = open(sys.argv[1], "r")
    line = inf.readline()
    count = 0
    while count < NUM_LINES and line != "":
        line = line.rstrip()
        count +=1
        print(line)
        line = inf.readline()
    inf.close()
except IOError as e:
    print("An error occurred while accessing the file. ", e)




