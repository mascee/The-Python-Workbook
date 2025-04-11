# This program simulates a coin toss and finds what is a minimum number
# of flips you need to have the same outcome 3 times in a row.
# What is the maximum number of times. And what is average.

import random

print("Coin toss simulation. ")

three_in_a_row = 0
total = 0

for i in range(1, 11): 
    count = 0
    consecutive = 1
    last_flip = random.choice(['T', 'H'])
    print(f"\nSimulation {i}:")
    print(last_flip)

    while consecutive < 3:
        flip = random.choice(['T', 'H'])
        print(flip)
        count += 1

        if flip == last_flip:
            consecutive += 1
        else:
            consecutive = 1
            last_flip = flip

    total_flips = count + 1
    print(f"It took {total_flips} to get 3 in a row. ")
    three_in_a_row += 1
    total += total_flips

average = total/three_in_a_row
print(f"\nAverage flips to get 3 in a row: {average:.2f}")
    

