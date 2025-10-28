from .pot import Pot
from .flop import Flop
from .game_object import GameObject

<<<<<<< HEAD
class Player(Flop,Pot) :
=======
class Player(GameObject):
>>>>>>> ded9290d3166a5e5e24e4388516e4262a064f442

    def __init__(self,name : str ,stack : int, is_ia : bool = False) -> None :
        """Initializing the Player """
        self._name = name
        self._stack = stack
        self.is_ia = is_ia

        self.main = []
        self.has_folded = False

    def fold(self,B : bool) -> bool:
        """Checking if the player folds or not"""
        return(B)
    
    def is_raising(self,B : bool) -> bool :
        """Checking if the player raises or not"""
        return(B)
    
    def raising_price(self,price : int) -> tuple :
        """Taking the raise of the stack"""

        self._stack -= price
        return()
    
    def is_checking(self, B : bool) -> bool : 
        """Checking if the player checks or not"""
        return(B)

    def is_following(self, B : bool) -> bool :
        '''Checking if the player is following'''
        return(B)
    
    def following_price(self, price : float) -> tuple :
        '''Taking the following off the stack'''

        self._stack -= price
        return()
    
    def best_combinaison(self) -> int :
        pass


    def is_winning(self, B : bool) -> bool :
        """Checking if hte player wins or not"""
        return(B)
    
    def win(self) -> None :
        """Winning and adding the pot to the stack"""
        self._stack += self._value

        


    







        

        
        

        






