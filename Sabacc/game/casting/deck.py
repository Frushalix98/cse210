import random
from game.casting.card import Card

class Deck():
    """A set of paper cards with a numerical value
    """

    def __init__(self, cards_list = []):
            """Constructs a new instance of Card with a value attribute.

            Args:
                self (Deck): An instance of Deck.
                cards (Card): An instance of Card
            """
            self._deck = cards_list

    def add(self, item = Card(), index = 0):
        self._deck.insert(index, item)

    def draw(self):
        """Removes card from the top of deck and returns that card"""
        card = self._deck[0]
        self._deck.pop(0)
        return card
    
    def get_deck(self):
        return self._deck

    def get_top_card(self):
        return self._deck[0]

    def shuffle(self):
        self._deck = random.shuffle(self._deck)