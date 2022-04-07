from casting.player import Player
from casting.card import Card
from casting.die import Die
from casting.deck import Deck
from constants import *

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        
        # ----------
        #   SETUP
        # ----------

        # Dice
        self.dice = [Die(DIE_SIDES) for die in range(NUM_OF_DICE)]

        # Card Decks
        self.deck_pile = Deck()
        self.discard_pile = Deck()
        for value in range(1, DECK_SIZE_POSITIVE+1):
            card = Card(value)
            self.deck_pile.add(card)
            self.deck_pile.add(card)
            self.deck_pile.add(card)

        for value in range(1, DECK_SIZE_NEGATIVE+1):
            card = Card(value*-1)
            self.deck_pile.add(card)
            self.deck_pile.add(card)
            self.deck_pile.add(card)

        for cards in range(CARDS_ZEROES):
            self.deck_pile.add(Card())

        # Players
        self.player_list = []
        for player in range(NUM_OF_PLAYERS):
            player = Player()
            self.player_list.append(player)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.new_game()
        while self.is_playing:
            self.do_updates()
            self.do_outputs()
            self.get_inputs()
        exit()
    
    def new_game(self):
        """Prepares for a new game"""
        #self.deck_pile.shuffle()
        self.print_deck_pile()
        pass

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        pass

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        pass
       
    def do_updates(self):
        """Checks if letters guessed are correct

        Args:
            self (Director): An instance of Director.
        """
        pass

    def deal_to_players(self):
        """Fills the hands of players"""
        for player in self.player_list:
            for draw in STARTING_HAND_SIZE:
                card = self.deck_pile.draw()
                player.add_card(card)

    def roll_dice(self):
        """Rolls each die for a new value"""
        for die in self.dice:
            die.roll()
    
    def print_dice(self):
        """Prints Dice and values to console"""
        print(self.dice)
    
    def print_deck_pile(self):
        """Prints deck_pile with cards and their values to console"""
        print(self.deck_pile)
        print(len(self.deck_pile.get_deck()))