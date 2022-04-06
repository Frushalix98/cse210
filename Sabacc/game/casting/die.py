import random

class Die:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
    """

    def __init__(self, sides = 1):
        """Constructs a new instance of Die.

        Args:
            self (Die): An instance of Die.
            faces (int): Number of sides on die
        """
        self._value = 0
        self._faces = abs(sides)
        self._roll_results = []
        self.roll()

    def __str__(self):
        return "1d" + str(self._faces) +" - " + str(self._value)
    
    def __repr__(self):
        return self.__str__()

    def roll(self):
        """Generates a new random value and calculates the points for the die.
        
        Args:
            self (Die): An instance of Die.
        """
        self._value = random.randint(1, self._faces)
        self._roll_results.append(self._value)
    
    def get_roll(self):
        """Returns value of Die"""
        return self._value