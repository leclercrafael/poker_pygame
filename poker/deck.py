import itertools
import random
from .settings import *
from .card import Card

class Deck():

    def __init__(self) -> None :
        settings = Settings()
        self.cartes = [Card(value = value, color = color) for value, color in itertools.product(settings.VALEURS, settings.COULEURS)]
        self.shuffle()

    def shuffle(self) -> None : 
        random.shuffle(self.cartes)

    def draw_card(self) -> Card : 
        if self.cartes:
            return self.cartes.pop()
        else : 
            print('Deck is empty')
            return None


