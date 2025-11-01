from player import Player
from card import Card
from game_object import GameObject
from deck import Deck

class Dealer(GameObject):

    def __init__(self) -> None:
        super().__init__()
        self.deck = Deck()
        self.players = []
        self.pot = 0
        self.maximum_bet = 0
        self.flop = None
        self.game_state = 'preflop'

    def draw_card(self) -> Card :
        self.deck.draw_card()

    def nouvelle_main(self) -> None:
        self.deck = Deck().shuffle()
        self.player = []
        self.pot = 0
        self.maximum_bet = 0
        self.flop = None
        self.game_state = 'preflop'

    def lancer_preflop(self) -> None:
        

    def lancer_flop(self) -> None:
        pass

    def lancer_turn(self) -> None:
        pass

    def lancer_river(self) -> None:
        pass



