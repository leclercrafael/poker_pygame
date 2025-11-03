from .pot import Pot
from .game_object import GameObject
from .card import Card

class Player(GameObject):

    def __init__(self,name : str, stack : int, is_ia : bool = False) -> None :
        """Initializing the Player """
        super().__init__()
        self._name = name
        self._stack = stack
        self.is_ia = is_ia
        self.main : list[Card] = []
        self.has_folded = False
        self.is_allin = False
        self.current_bet = 0
        self

    def fold(self) -> None:
        """Player is folding"""
        self.has_folded = True

    def bet(self, amount : int) -> int : 
        '''Player is betting the amount proposed by an other player'''
        if amount >= self._stack:
            amount = self._stack
            self.is_allin = True
            print(f"{self._name} fait tapis avec {amount}!")
        elif amount<=0 :
            print('Mise invalide') 
            return 0
        
        self._stack -= amount
        self.current_bet += amount 
        print(f"{self._name} mise {amount}.")
        return amount

    def raise_bet(self, amount : int) -> int :
        '''Player is raising the pot'''

        total_needed = amount
        amount_to_add = total_needed - self.current_bet

        if amount_to_add >= self._stack :
            amount_to_add = self._stack
            self.is_allin = True
            print(f"{self._name} fait tapis en relançant!")

        elif amount_to_add <= 0:
             print("Relance invalide.")
             return 0

        self._stack -= amount_to_add
        bet_made = amount_to_add 
        self.current_bet += amount_to_add 
        print(f"{self._name} relance de {amount_to_add} (total {self.current_bet}).")
        return bet_made 
    
    def call_bet(self, amount : int) -> int :
        '''Player is calling an other one'''

        if amount >= self._stack:
            amount = self._stack
            self.is_allin = True
            print(f"{self._name} is all in by calling")
        elif amount <= 0:
            print('Invalid call')
            return 0
        
        self._stack -= amount
        self.current_bet += amount 
        print(f"{self._name} calls {amount}.")
        return amount
    
    def check(self) -> int :
        '''Player is checking'''
        print(f"{self._name} checks")
        return 0
    

    def receive_cards(self, card : Card) -> None :
        """Add card to the hand"""
        if len(self.main)<2:
            self.main.append(card)

    def reset_for_new_hand(self) -> None :
        '''Reset the hand for the next hand'''
        self.main = []
        self.current_bet = 0
        self.has_folded = False
        self.is_allin = False

    def collect_winnings(self, amount : int) -> None:
        """Collect the chips after winning and add them to the stack"""
        if amount > 0:
            self._stack += amount
            print(f"{self._name} wins {amount}!")

    def draw(self) -> None:
        """Draw the cards"""
        if self.has_folded :
            return

        # Checking if the cards where configurated with set_display
        if not self.main:
            return 

        # Drawing the cards
        for card in self.main:
            card.draw()
    
    def random_ia(self) -> None :
        """Decision tree of the player IA"""

