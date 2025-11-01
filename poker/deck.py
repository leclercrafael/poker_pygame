import itertools
import random
from settings import *
from card import Card

d_pos = { "1" : [50,100], "2" : [110,100]}

class Deck():

    def __init__(self) -> None :
        settings = Settings()
        self.cartes = [Card(screen=self.screen, d_pos=d_pos, position='1', size=100,
                            value = valeur, color = couleur) for valeur, couleur in itertools.product(settings.VALEURS, settings.COULEURS)]
        self.shuffle()

    def shuffle(self) -> None : 
        random.shuffle(self.cartes)

    def draw_card(self) -> Card : 
        if self.cartes:
            return self.cartes.pop()
        else : 
            print('Deck is empty')
            return None


