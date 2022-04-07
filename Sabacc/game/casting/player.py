from constants import *
from casting.deck import Deck

class Player():
    """A person who plays in the game. 
    s
    Attributes:
        is_playing (boolean): Whether or not the game is being played.
    """

    def __init__(self, chips = 0, hand = Deck()):
        """Constructs a new instance of Player
        
        Args:
            self (Player): An instance of Player
        """
        self._hand = hand
        self._chips = chips

    def get_hand(self):
        return self._hand
    
    def add_card(self, card):
        self._hand.add(card)
    
    def give_card(self):
        card = self._hand[0]
        self._hand.pop(0)
        return card
    
    def get_chips(self):
        return self._chips

    def add_chips(self, amount = int()):
        self._chips += amount

    def pay_chips(self, amount = int()):
        self._chips -= amount

