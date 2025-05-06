# Testing command files

import sys


print(f"The program has {len(sys.argv)} command line arguments. ")
print(f"The name of the .py file is {sys.argv[0]}")

if len(sys.argv) > 1:
    print("The remaining arguments are: ")
    for i in range(1, len(sys.argv)):
        print(" ", sys.arg[i])
else:
    print("No additional arguments were provided. ")