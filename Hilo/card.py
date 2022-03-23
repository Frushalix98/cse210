class Card:
    
    def __init__(self, value, suit):
        self.value= value
        self.suit = suit
        self.face = ''
        if value == 1:
            self.face = 'Ace'
        elif value == 11:
            self.face = 'Jack'
        elif value == 12:
            self.face = 'Queen'
        elif value == 13:
            self.face = 'King'
        else:
            self.face = self.value
    def __str__(self) -> str:
        return (f'{self.face} of {self.suit}')

    def get_value(self):
        return self.value