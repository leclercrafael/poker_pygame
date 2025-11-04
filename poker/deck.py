import itertools
import random
from settings import *
from card import Card

class Deck():

    def __init__(self) -> None :
        """Initialize the deck"""
        settings = Settings()
        self.cartes = [Card(value = value, color = color) for value, color in itertools.product(settings.VALEURS, settings.COULEURS)]
        self.shuffle()

    def shuffle(self) -> None : 
        """Shuffle the deck"""
        random.shuffle(self.cartes)


    def is_empty(self) -> bool:
        """Checking if the deck is empty"""
        if len(self.cartes) == 0 :
            print("Deck is empty")
        return(len(self.cartes) == 0)
        

    def draw_card(self) -> Card : 
        if not self.is_empty(): # Ajoute cette vérification
            return self.cartes.pop()
        else:
            print("Erreur : Le deck est vide, impossible de tirer.")
            return None # Retourne None si c'est vide


