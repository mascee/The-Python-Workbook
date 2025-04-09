# A parity bit is a simple mechanism for detecting errors in data transmitted over
# an unreliable connection such as a telephone.
# The basic idea is that an additional bit is transmitted 
# after each group of 8 bits so that a single bit error in the transmission can be detected.
# Parity bits can be computed for either even parity or odd parity.
# If even parity is selected then the parity bit that is transmitted is chosen so that 
# the total number of one bit trasmitted is odd.

# This program computes the parity bit for groups of 8 bits entered by the user using even parity.
# The program reads strings containing 8 bits until the user enters a blank like.
# After each string is entered by the user the program dusplays a clear message indicating whether 
# the parity bit should be 0 or 1.


binary_string = input("Enter 8 bits - zeros and 1s: ")

while binary_string != "": 
    if binary_string.count('0') + binary_string.count('1') != 8 or len(binary_string) != 8:
        print("This wasn't 8 bits. Try again")
    else:
        ones = binary_string.count('1')

    if ones % 2 == 0:
        print("The parity bit should be 0. ")
    else:
        print("The parity bit should be 1. ")

    binary_string = input("Enter 8 bits - zeros and 1s: ")
