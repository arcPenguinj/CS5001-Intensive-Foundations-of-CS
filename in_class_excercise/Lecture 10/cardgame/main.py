from deckofcards import  DeckOfCards
from stack import Stack

def main():
    deck = DeckOfCards()
    deck.shuffle()

    # Each player's "hand" - the cards they can play
    player1_hand = Stack()
    player2_hand = Stack()

    # Deal all cards to the two players
    while deck.num_cards_in_deck() > 0:
        player1_hand.push(deck.draw_card())
        player2_hand.push(deck.draw_card())

    # As long as no one has run out of cards...play a turn
    while player1_hand.is_empty() == False and player2_hand.is_empty() == False:
        # Both players look at the card on top of their hand
        player1_card = player1_hand.peek()
        player2_card = player2_hand.peek()

        # If both cards have equal value, both players remove their top cards.
        # Otherwise the player with the lowest value card removes it from their
        # hand.
        print("Player 1 has the", player1_card, "and Player 2 has the", player2_card)
        if player1_card.value == player2_card.value:
            player1_hand.pop()
            player2_hand.pop()
            print("Tie. Both players remove their cards.")
        elif player1_card.value < player2_card.value:
            player1_hand.pop()
            print("Player 2 beats player 1. Player 1 removes their card.")
        else:
            player2_hand.pop()
            print("Player 1 beats player 2. Player 2 removes their card.")
        input("Press any key to play the next round\n\n")
    
    # The game is over. Announce the winner  (the player with the most cards).
    if player1_hand.size() == player2_hand.size():
        print("IT'S A TIE")
    elif player1_hand.size() > player2_hand.size():
        print("PLAYER 1 WINS")
    else:
        print("PLAYER 2 WINS")


if __name__ == "__main__":
    main()
     