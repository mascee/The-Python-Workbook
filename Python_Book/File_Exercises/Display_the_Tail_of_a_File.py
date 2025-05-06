# Unix-based operating systems also typically include a tool named "tail".
# It displays the last 10 lines of a file whose name is provided as a command line 
# argument.
# This program implements this

import sys
print(sys.argv)

NUM_LINES = 10

if len (sys.argv) != 2:
    print("Provide a file name as a command line argument. ")
    quit()

try:
    inf = open(sys.argv[1], "r")
    lines = []
    for line in inf:
        lines.append(line)
        if len(lines) > NUM_LINES:
            lines.pop(0)
    inf.close()
except IOError as e:
    print("Error occured while processing the file. ")
    quit()

for line in lines:
    print(line, end= "")


    