from constants import *
from casting.deck import Deck
from casting.card import Card

class Player():
    """A person who plays in the game. 
    s
    Attributes:
        is_playing (boolean): Whether or not the game is being played.
    """

    def __init__(self, name = str(), chips = 0, hand = Deck()):
        """Constructs a new instance of Player
        
        Args:
            self (Player): An instance of Player
        """
        self._name = name
        self._hand = hand
        self._chips = chips

    def __str__(self):
        return "Name: " + self._name + ", Chips: " + str(self._chips) + ", Hand: " + str(self._hand)
    
    def __repr__(self):
        return self.__str__()

    def get_hand():
        return self._hand
    
    def add_card(self, card = Card()):
        self._hand.add(card)
    
    def give_card(self):
        card = self._hand[0]
        self._hand.pop(0)
        return card
    
    def get_chips():
        return self._chips

    def add_chips(self, amount = int()):
        self._chips += amount

    def pay_chips(self, amount = int()):
        self._chips -= amount
    
    def get_name(self):
        return self._name
    
    def set_name(name = str()):
        self._name = name

