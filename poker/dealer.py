from player import Player
from card import Card
from game_object import GameObject
from deck import Deck
from settings import *

class Dealer(GameObject):

    def __init__(self) -> None:
        super().__init__()
        self.deck = Deck()
        self.settings = Settings()
        self.players : list[Player]= []
        self.pot = 0
        self.maximum_bet = 0
        self.flop : list[Card] = []
        self.game_state = 'preflop'
        self.current_player_index=0
        self.betting_round_active = True
        self.winning : int = 10000

    
    def add_player(self, player : Player) -> None:
        if player not in self.players:
            self.players.append(player)

    def nouvelle_main(self) -> None:
        self.flop = []
        self.deck = Deck()
        self.pot = 0
        self.maximum_bet = 0
        self.game_state = 'preflop'


        for player in self.players:
            player.reset_for_new_hand()

        sb_player = self.players[0]
        sb_amount = self.settings.SMALL_BLIND # Récupère la valeur depuis Settings
        bet_made_sb = sb_player.bet(sb_amount) # Utilise la méthode 'bet'
        self.pot += bet_made_sb
        
        # Le joueur 1 (IA) paie la Big Blind
        bb_player = self.players[1]
        bb_amount = self.settings.BIG_BLIND
        bet_made_bb = bb_player.bet(bb_amount)
        self.pot += bet_made_bb

        # La mise à suivre pour le premier joueur (Humain) est la Big Blind
        self.maximum_bet = bb_amount 
        
        # Le premier à parler est le joueur 0 (SB)
        self.current_player_index = 0

    def draw_card(self) -> Card :
        return self.deck.draw_card()

    def draw_new_hand(self) -> None:
        'We want to draw a new hand for each player'
        for _ in range(2):
            for player in self.players:
                if not player.has_folded:
                    if not self.deck.is_empty() :
                        card = self.draw_card()
                        if card:
                            player.receive_cards(card)
                    else: 
                        print("Deck is empty")


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

            bet_made = player.raise_bet(amount)
            self.pot += bet_made
            self.maximum_bet = player.current_bet

        self.next_player_turn()

    

    def player_win(self) -> None :
        """Retain who wins"""
        
        self.winning = self.current_player_index

    def create_flop(self) -> None :
        """Creating the flop"""

        for i in range(5):
            if not self.deck.is_empty():
                c = self.draw_card()
                self.flop.append(c)
                print(f"La carte est le {c._value} de {c._color_name}" )
            else : 
                print("deck is empty")

       
        
     
    
    def flop_draw(self, n : int ):
        """Drawing on the figure the cards from the flop"""

        if not self.flop:
            return 

        
        for card in self.flop[:n]:
            card.draw()

    
    def lancer_flop(self) -> None:

        print("--- DÉBUT DU FLOP ---")
        self.draw_card() # Brûle une carte (on ne la stocke pas)
        for _ in range(3):
            card = self.draw_card()
            if card:
                self.flop.append(card)

        self.betting_round_active = True
        self.current_player_index = 0 # Le joueur 0 (SB) parle en premier
        self.maximum_bet = 0 # Nouveau tour de mise


    def lancer_turn(self) -> None:
        """Brûle une carte et révèle le Turn."""
        print("--- DÉBUT DU TURN ---")
        self.draw_card() # Brûle une carte
        card = self.draw_card()
        if card:
            self.flop.append(card) # Ajoute la 4ème carte

        self.betting_round_active = True
        self.current_player_index = 0
        self.maximum_bet = 0
        

    def lancer_river(self) -> None:
        """Brûle une carte et révèle la River."""
        print("--- DÉBUT DU RIVER ---")
        self.draw_card() # Brûle une carte
        card = self.draw_card()
        if card:
            self.flop.append(card) # Ajoute la 5ème carte

        self.betting_round_active = True
        self.current_player_index = 0
        self.maximum_bet = 0



    def next_player_turn(self):
        """Passe au joueur suivant et vérifie si le tour de mise est terminé."""

        # Logique simple pour 2 joueurs
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

        p0 = self.players[0]
        p1 = self.players[1]

        # Le tour se termine si :
        # 1. Un joueur est all-in
        # 2. Un joueur s'est couché
        # 3. Les deux joueurs ont misé le même montant (et le tour est revenu au début)

        round_over = False
        if p0.is_allin or p1.is_allin:
            round_over = True
        elif p0.has_folded or p1.has_folded:
            round_over = True
        elif p0.current_bet == p1.current_bet:
            round_over = True

        if round_over:
            print(f"Fin du tour de mises pour : {self.game_state}")
            self.end_betting_round()

    def end_betting_round(self):
        """Termine le tour de mise et passe à l'état suivant."""
        self.betting_round_active = False
        self.current_player_index = 0 
        self.maximum_bet = 0

        for player in self.players:
            player.current_bet = 0 # Réinitialise les mises du tour

        # Logique de passage à l'état suivant
        if self.game_state == 'preflop':
            self.game_state = 'flop'
            self.lancer_flop()
        elif self.game_state == 'flop':
            self.game_state = 'turn'
            self.lancer_turn()
        elif self.game_state == 'turn':
            self.game_state = 'river'
            self.lancer_river()
        elif self.game_state == 'river':
            self.game_state = 'showdown'
            # (Ici on comparera les mains)



    def draw(self) -> None :
            pass



    
    """
    def reveal_flop(self):
        c = self.flop.pop()
        return (c)
 """    


