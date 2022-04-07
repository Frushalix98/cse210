import random
from casting.card import Card

class Deck():
    """A set of paper cards with a numerical value
    """

    def __init__(self, cards_list = []):
            """Constructs a new instance of Card with a value attribute.

            Args:
                self (Deck): An instance of Deck.
                cards (Card): An instance of Card
            """
            self._deck = []
            if len(cards_list) > 0:
                self._deck = cards_list

    def __str__(self):
        return str(self._deck)
    
    def __repr__(self):
        return self.__str__()

    def add(self, item, index = 0):
        self._deck.insert(index, item)

    def draw(self):
        """Returns top card in list"""
        return self._deck[0]
    
    def get_deck(self):
        return self._deck
    
    def set_deck(self, cards_list = list()):
        self._deck = cards_list

    def get_top_card(self):
        return self._deck[0]

    def shuffle(self):
        random.shuffle(self._deck)