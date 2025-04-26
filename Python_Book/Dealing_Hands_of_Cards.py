# Excercise 126. Dealing Hands of Cards
# This program has a function "deal", which takes the number of hands, the number of cards per hand,
# and a deck of cards as its three parameters.
# The function returns a list containing all of the hands that were dealt.
# Each hand is represented as a list of cards.

from Shuffling_a_Deck_of_Cards import createDeck, shuffle

def deal(num_hands, num_cards, deck):
    # Create and shuffle deck
    shuffled_deck = shuffle()

    hands = []
    for _ in range(num_hands):
        hand = []
        for _ in range(num_cards):
            if shuffled_deck:
                hand.append(shuffled_deck.pop(0))  # Deal the top card
        hands.append(hand)

    return hands



def main():
    deck = createDeck()  # Create a full deck
    hands = deal(5, 6, deck)  # Deal 5 hands, 6 cards each
    for i, hand in enumerate(hands, 1):
        print(f"Hand {i}: {hand}")

if __name__ == "__main__":
    main()