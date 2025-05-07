# Exercise 155. Words that Occur Most.
# This program determines words that occur most in the file

import sys

MAX_FREQUNCY = 5

if len(sys.argv) != 2:
    print("Provide a file name as a command line argument. ")
    quit()

try:
    inf = open(sys.argv[1], "r")
    most_popular = []
    print(f"Words that occur the most: {most_popular}. ")
    inf.close()


except IOError as e:
    print("Error occured while processing the file. ")
    quit()