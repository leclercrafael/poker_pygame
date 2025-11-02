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
        self.current_player_index=0
        self.betting_round_active = True
    
    def add_player(self, player : Player) -> None:
        if player not in self.players:
            self.players.append(player)

    def nouvelle_main(self) -> None:
        self.pot = 0
        self.maximum_bet = 0
        self.flop = None
        self.game_state = 'preflop'

        for player in self.players:
            player.reset_for_new_hand()

    def draw_card(self) -> Card :
        return self.deck.draw_card()

    def draw_new_hand(self) -> None:
        'We want to draw a new hand for each player'
        for _ in range(2):
            for player in self.players:
                if not player.has_folded:
                    card = self.draw_card()
                    if card:
                        player.receive_cards(card)


    def player_action(self, action:str, amount=0) -> None:

        try:
            player = self.players[self.current_player_index]
        except IndexError:
            print("Erreur : Index du joueur non valide")
            return
        
        if action == 'fold':
            player.fold()

        elif action =='check':
            if self.maximum_bet == player.current_bet:
                player.check()
            else:
                print(f"Impossible to check, bet to follow {self.maximum_bet}")
        
        elif action == 'call':
            amount_to_call = self.maximum_bet - player.current_bet
            bet_made = player.call_bet(amount_to_call)
            self.pot += bet_made

        elif action == 'raise':
            if amount < 2*self.maximum_bet and not(player.is_allin):
                print('Amount of raise is not enough, you must raise min 2 time maximum bet')
                return

            bet_made = player.call_bet(amount)
            self.pot += bet_made
            self.maximum_bet = player.current_bet

        self.next_player_turn()





    def lancer_preflop(self) -> None:
        pass

    def lancer_flop(self) -> None:
        pass

    def lancer_turn(self) -> None:
        pass

    def lancer_river(self) -> None:
        pass
    def draw(self) -> None:
        pass



