# Exercise 146. Create a Bingo Card.
# A Bingo Card consists of 5 columns of 5 numbers which are labeled 
# with letters: BINGO.
# There are 15 numbers that can appear under each letter.
# In particular, the numbers can appear under the B range from 1 to 15, 
# the numbers can appear under the I range from 16 to 30, the numbers that can appear under the N range
# from 31 to 45, and so on.
# Write a function that creates a random Bingo card and stores it in a dictionary.
# The keys will be letters B, I, N, G, O.
# The values are numbers.
# Write a second funciton that displays the Bingo card with columns labeled properly.


from random import randrange
NUMS_PER_LETTER = 15

def createCard():
    card = {}

    lower = 1
    upper = 1 + NUMS_PER_LETTER

    for letter in ["B", "I", "N", "G", "O"]:
        #Empty list for a letter
        card[letter] = []

        while len(card[letter])!= 5:
            next_num = randrange(lower, upper)
            #Ensure there are no duplicates
            if next_num not in card[letter]:
                card[letter].append(next_num)
    
        #Update the range of values
        lower += NUMS_PER_LETTER
        upper += NUMS_PER_LETTER

    return card


def displayCard(card):
    print("B  I  N  G  O")
    for i in range(5):
        for letter in ['B', 'I', 'N', 'G', 'O']:
            print("%2d" % card[letter][i], end=" ")
        print()


def main():
    card = createCard()
    displayCard(card)


if __name__ == "__main__":
    main()
