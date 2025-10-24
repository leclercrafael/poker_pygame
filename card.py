from .game_object import GameObject

class Card(GameObject) :

    def __init__(self,number : int ,color : tuple ) -> None :
        """Initialize the Object"""
        super().__init__()
        self._number = number
        self._color = color

    @property
    def value(self) -> tuple : 
        return ((self._number,self._color))
    
    
                
