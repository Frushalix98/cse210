from constants import *
from casting.deck import Deck

class Player():
    """A person who plays in the game. 
    s
    Attributes:
        is_playing (boolean): Whether or not the game is being played.
    """

    def __init__(self, hand = Deck()):
        """Constructs a new instance of Player
        
        Args:
            self (Player): An instance of Player
        """
        self._hand = hand

    def get_hand(self):
        return self._hand
    
    def add_card(self, card):
        self._hand.add(card)

