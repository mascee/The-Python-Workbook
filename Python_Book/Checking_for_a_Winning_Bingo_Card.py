# Exercise 147. Checking for a Winning Card.
# A winning Bingo card contains a line of 5 numbers that have all been called.
# Players normally record the numbers that have been called by crossing them out or marking
# them with a Bingo dauber. In this exercise we will mark that number has been called by replacing it with a 0
# in the Bingo card dictionary.
# Write a function that takes a dictionary representing a Bingo Card as its only
# parameter. If the card contains a line of zeros (vertical, horizontal or diagonal) then the function 
# should return True, indicating that the card has won.
# Otherwise the function should return False.

from Create_a_Bingo_Card import createCard, displayCard

def Bingo(card):
    # Convert dictionary to a grid (list of rows)
    grid = []
    for i in range(5):
        row = [card[column][i] for column in "BINGO"]
        grid.append(row)

    # Check horizontal lines
    for row in grid:
        if all(num == 0 for num in row):
            return True

    # Check vertical lines
    for col in range(5):
        if all(grid[row][col] == 0 for row in range(5)):
            return True

    # Check diagonals
    if all(grid[i][i] == 0 for i in range(5)):
        return True
    if all(grid[i][4 - i] == 0 for i in range(5)):
        return True

    return False

def main():
    card = createCard()

    # Simulate a winning diagonal
    for i, col in enumerate("BINGO"):
        card[col][i] = 0

    result = Bingo(card)
    if result:
        print("Bingo!")
    else:
        print("No Bingo yet.")

    displayCard(card)



if __name__ == "__main__":
    main()
