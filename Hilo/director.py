from timeit import repeat
from card import Card
import random

class Director:
    def __init__(self):
        self.current_deck = []
        self.cards_in_deck = 52
        self.points = 300
        self.win = 500
        self.lose = 0
        self.wrong = -75
        self.correct = 100
        self.suit_list = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        self.face = ['Ace', 'Jack', 'Queen', 'King']
        self.is_playing = True


        # Creates deck of cards
        for suit in self.suit_list:
            for value in range(13):
                card = Card(value+1, suit)                
                self.current_deck.append(card)
        # Shuffles the deck we just
        random.shuffle(self.current_deck)

        self.current_card = self.current_deck[0]
        self.second_card = self.current_deck[1]
        
            

    def start_game(self):
        # If Win Condition has not been met
        while self.is_playing == True:
            # Turn Order
            self.updater()
            self.output()
            self.player_input()
            
        print('Good game!')

    def player_input(self):
        if not self.is_playing:
            return

        repeat_player_input = True
        while repeat_player_input == True:
            player_input = input("Higher or Lower? (h/l)\n")
            if (player_input).lower() == "h":
                if self.current_card.get_value() < self.second_card.get_value():
                    
                    self.points += 100
                    
                else:
                    self.points -= 75
                repeat_player_input = False
            elif player_input.lower() == "l":
                if self.current_card.get_value() > self.second_card.get_value():
                    self.points += 100
                else:
                    self.points -= 75
                
                repeat_player_input = False
            else:
                print("That is not higher or lower.")
        print(f'The next card was {self.second_card}')
        print(f'Your points have been updated to {self.points}')
        
        if self.points <= 0:
            self.is_playing = False
            return

        yes_or_no = True
        while yes_or_no == True:
            replay_again_again_again = input('Would you like to play again? (y/n)\n')
            if replay_again_again_again.lower() == 'y':
                yes_or_no = False
            elif replay_again_again_again.lower() == 'n':
                yes_or_no = False
                self.is_playing = False
            else:
                self.yes_or_no = True
        

    def updater(self):
        if not self.is_playing:
            return
        self.current_deck.remove(self.current_deck[0])
        self.current_deck.append(self.current_card)
        self.current_card = self.current_deck[0]
        self.second_card = self.current_deck[1]
        
        


    def output(self):
        if not self.is_playing:
            return
        print(f'The top card is {self.current_card}')
