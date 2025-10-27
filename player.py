from .hand import Hand 
from .pot import Pot
from .flop import Flop

class Player(Hand,Flop) :

    def __init__(self,name : str ,stack : int) -> None :
        """Initializing the Player """
        super().__init__()
        self._name = name
        self._stack = stack

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
    
    def best_combinaison(self) -> int :
        


    







        

        
        

        






