# Excercise 121. Random Lottery numbers
# In order to win the top prize in a particular lottery, one must match
# all 6 numbers on his or her ticket to the 6 numbers between 1 and 49 that 
# are drawn by the lottery organizer.
# This program generates a random selection of 6 numbers for a lottery ticket.
# Ensures that the 6 numbers selected do not contain any duplicates and displays the
# numbers in ascending order

from random import randrange

NUM_MIN = 1
NUM_MAX = 49
NUM_NUMS = 6

ticket = []

for i in range(NUM_NUMS):
    rand = randrange(NUM_MIN, NUM_MAX + 1)
    while rand in ticket:
        rand = randrange(NUM_MIN, NUM_MAX + 1)
    ticket.append(rand)

ticket.sort()
print("Your numbers are: ")
for n in ticket:
    print(n, end=" ")
print()
