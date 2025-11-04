from .card import Card
from .deck import Deck


class Flop():

    def __init__(self, flop : list) -> None :
        """Initialize the variables"""
        self._flop = flop
        

    def add_card(self) -> None :
        """Add a card to the flop"""
        self._flop.append(Deck.draw_card(self))

    def draw(self) -> None :
        for c in self._flop :
            pos = D_POS["joueur_main"][i] # Récupère la position [x, y]
            c.set_display(screen=self.screen, x=pos[0], y=pos[1], size=120)
            c.retourner() # On retourne les cartes du joueur


    

    
    
