# Exercise 172. Words with Six Vowels in Order.
# There is at least one word in the English language that contains each of the
# vowels A, E, I, O, U, Y exactly ones and in order. 
# Write a program that searches a file containing a list of words and displays all the words
# that meet this constraint. The user will provide the name of the file that will be searched.
# Display an appropriate error message and exit the program if the user provides an invalid file words
# with six vowels in order.

from sys import argv

if len(argv) != 2:
    print("Provide a Python file to review in the command line.")
    quit()
fname = argv[1]

vowels = ["A", "E", "I", "O", "U", "Y"]
try:
    with open(fname, "r") as inf:
        for line in inf:
            word = line.strip().lower().split()

