# Exercise 137. Two dice simulation.
# This program simulates 1000 rolls of two dice.

from random import randrange

NUM_RUNS = 1000
D_MAX = 6

#Function that simulates rolling a pair of six-sided dice.
def roll_two_dice():
    # Roll first die
    d1 = randrange(1, D_MAX +1)
    # Roll second die
    d2 = randrange(1, D_MAX +1)
    #Return total    
    return d1 + d2

def main():
    #Express the frequency for each total as a percentage of the number of roll performed.
    
    # Expected percent
    expected = {2: 1/36,
                3: 2/36,
                4: 3/36,
                5: 4/36,
                6: 5/36,
                7: 6/36,
                8: 5/36,
                9: 4/36,
                10: 3/36,
                11: 2/36,
                12: 1/36
                }
    

    #Create a dictionary that maps from the total of two dice to the number of occurences.
    counts = {
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0
    }    

    for i in range(NUM_RUNS):
        t = roll_two_dice()
        counts[t] = counts[t] + 1

    print("Total simulated proportions and the expected proportions: ")
    for i in sorted(counts.keys()):
        print(f"{i:5d} {counts[i]/NUM_RUNS*100:11.2f} {expected[i]*100:8.2f}")


if __name__ == "__main__":
    main()