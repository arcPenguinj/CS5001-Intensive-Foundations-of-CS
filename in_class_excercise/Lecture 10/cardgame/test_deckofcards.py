from deckofcards import DeckOfCards
from playingcard import PlayingCard


def test_draw_cards():
    deck = DeckOfCards()
    assert(deck.num_cards_in_deck() == 52)
    assert(deck.draw_card() == PlayingCard(13, "Clubs"))
    assert(deck.num_cards_in_deck() == 51)