# Exercise 148. Play Bingo
# This program simulates a game of Bingo for a single card.
# Begin by generating a list of all the valid Bingo cards (B1 through O75)
# Once the list has been created randomize the order of its elements calling shuffle function in the
# random module.
# Then the program should consume calls out of the list and cross out numbers on the card contains a winning line.
# Simulate 1000 games and report the minimum, maximum and average number of calls that must be made before the card wins.

from random import shuffle
from Create_a_Bingo_Card import createCard, displayCard
from Checking_for_a_Winning_Bingo_Card import Bingo

NUMS_PER_LETTER = 15

# Function to generate list of all Bingo calls: "B1" to "O75"
def generateCalls():
    calls = []
    letters = ["B", "I", "N", "G", "O"]
    for i, letter in enumerate(letters):
        start = i * NUMS_PER_LETTER + 1
        end = start + NUMS_PER_LETTER
        for num in range(start, end):
            calls.append(f"{letter}{num}")
    return calls

# Function to mark a number on the card (replace it with 0)
def markCard(card, call):
    letter = call[0]
    number = int(call[1:])
    if number in card[letter]:
        index = card[letter].index(number)
        card[letter][index] = 0

# Simulate a single game, return number of calls until Bingo
def simulateOneGame():
    card = createCard()
    calls = generateCalls()
    shuffle(calls)

    for i, call in enumerate(calls, 1):
        markCard(card, call)
        if Bingo(card):
            return i  # Number of calls taken to win
        
# Main simulation
def main():
    NUM_SIMULATIONS = 1000
    results = []

    for _ in range(NUM_SIMULATIONS):
        calls_needed = simulateOneGame()
        results.append(calls_needed)

    print(f"Minimum calls until Bingo: {min(results)}")
    print(f"Maximum calls until Bingo: {max(results)}")
    print(f"Average calls until Bingo: {sum(results)/len(results):.2f}")

if __name__ == "__main__":
    main()