from .card import Card

class Flop():

    def __init__(self, flop : list) -> None :
        """Initialize the variables"""
        self._flop = flop


    def add_card(self, value : int , color : str) -> None :
        """Add a card to the flop"""
        self._flop.append(Card(value = value ,color = color))

    

    
    
