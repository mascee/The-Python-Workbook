# Excercise 125. Shuffling a Deck of Cards
# Each deck of cards is 52 cards. Each card has one of four suits along with a value.
# The suits are normally spades, hearts, diamonds and clubs while the valuse are 2 through 10, Jack, Queen, King and Ace.
# Each playing card can be represented by two characters - values (2-9), characters (T, J, Q, K and A) that represent values of 
# 10, Jack, Queen, King and Ace. The second character is used to represent the suit of the cards- "s", "h", "d" and "c". 
# This program has a function createDeck that crates a deck of cards. 
# There is a function shuffle that randomizes order of the cards.
# Main displays deck of cards before and after shuffle.
import random


def createDeck():
    deck = []
    suits = ['s', 'h', 'd', 'c']
    values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    deck = [value+suit for suit in suits for value in values]
    return deck

def shuffle():
    deck = []
    deck = createDeck()
    random.shuffle(deck)
    return deck

def main():
    print("This is a deck of cards: ")
    print(createDeck())
    print("*****************************************************************************************************************")
    print("This is a suffled deck: ")
    print(shuffle())


if __name__ == "__main__":
    main()


