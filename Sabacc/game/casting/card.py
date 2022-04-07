class Card():
    """A paper card with a numerical value
   
    Attributes:
        value (int): The number on a card.
    """

    def __init__(self, value = 0):
            """Constructs a new instance of Card with a value attribute.

            Args:
                self (Card): An instance of Card.
            """
            self._value = value

    def get_value(self):
        return self._value

    def __str__(self):
        return str(self._value) 
    
    def __repr__(self):
        return self.__str__()