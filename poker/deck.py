import itertools
import random
from settings import *
from card import Card

class Deck():

    def __init__(self) -> None :
        settings = Settings()
        self.cartes = [Card(valeur, couleur) for valeur, couleur in itertools.product(settings.VALEURS, settings.COULEURS)]
        self.melanger()

    def melanger(self) -> None : 
        random.shuffle(self.cartes)

    def tirer(self) -> Card : 
        if self.cartes:
            return self.cartes.pop()
        else : 
            print('Le jeu est vide')
            return None


