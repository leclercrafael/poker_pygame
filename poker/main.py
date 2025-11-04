from settings import Settings
import ctypes, pygame, sys
# from card import Card # Plus besoin d'importer Card ici
# from deck import Deck # Plus besoin d'importer Deck ici
from dealer import Dealer
from player import Player # <-- AJOUTER L'IMPORT DU JOUEUR

D_POS = {
    "joueur_main": [[50, 500], [180, 500]], 
    "ia_main": [[50, 100], [180, 100]],
    "flop" : [[500,300],[630,300],[760,300],[890,300],[1020,300]]
}


__name__ = "__main__"

class Game(Settings):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption(self.TITLE_STRING)
        self.clock = pygame.time.Clock()

        self.dealer = Dealer()
        self.Flop = False
        
        # Création des joueurs
        self.joueur_humain = Player(name="Player", stack=1000, is_ia=False)
        self.joueur_ia = Player(name="IA", stack=1000, is_ia=True)
        
        # Le Dealer connaît ses joueurs
        self.dealer.add_player(self.joueur_humain)
        self.dealer.add_player(self.joueur_ia)

        # Lancement de la première main
        self.dealer.nouvelle_main() # Prépare le deck et les joueurs
        self.dealer.draw_new_hand() # Distribue 2 cartes logiques
    
        
        for i, card in enumerate(self.joueur_humain.main):
            pos = D_POS["joueur_main"][i] # Récupère la position [x, y]
            card.set_display(screen=self.screen, x=pos[0], y=pos[1], size=120)
            card.retourner() # On retourne les cartes du joueur

        for i, card in enumerate(self.joueur_ia.main):
            pos = D_POS["ia_main"][i]
            card.set_display(screen=self.screen, x=pos[0], y=pos[1], size=120)
                  
        


        #UI

        self.bouton_fold_rect = pygame.Rect(500, 800, 200, 70)
        self.bouton_check_rect = pygame.Rect(750, 800, 200, 70)
        self.bouton_call_rect = pygame.Rect(1000, 800, 200, 70)
        self.bouton_raise_rect = pygame.Rect(1250, 800, 200, 70)

        self.bouton_stack1 = pygame.Rect(350, 500, 100, 70)
        self.bouton_stack2 = pygame.Rect(350, 100, 100, 70)

# --- Variables pour la saisie de la relance ---
        self.is_raising = False      # État : sommes-nous en train de saisir une relance ?
        self.raise_input_text = ""   # Le texte en cours de saisie
        # Un rectangle pour la zone de saisie
        self.raise_input_rect = pygame.Rect(750, 100, 100, 40) 
        self.color_active = pygame.Color('dodgerblue2')
        self.color_inactive = pygame.Color('lightgray')
        self.input_box_color = self.color_inactive
        self.font = pygame.font.SysFont('Arial', 30)
        self.small_font = pygame.font.SysFont('Arial', 24)



        self.Flop = False


        try:
            self.font_bouton = pygame.font.SysFont('arial', 30, bold=True)
        except pygame.error:
            self.font_bouton = pygame.font.Font(None, 36)


    # Dans main.py (MODIFIER run)
    def run(self):
        self.start_time = pygame.time.get_ticks()
        # (On peut ajouter les blinds ici, mais faisons simple pour l'instant)
        # self.dealer.lancer_preflop() # On le fera à l'étape suivante

        while True:
            # --- 1. GESTION DES ÉVÉNEMENTS ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # --- GESTION DES CLICS DE SOURIS (Simplifié) ---
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # C'est le tour du joueur humain ET le tour de mise est actif ?
                    if self.dealer.betting_round_active and self.dealer.current_player_index == 0 and not self.is_raising:

                        if self.bouton_fold_rect.collidepoint(event.pos):
                            print("CLIC SUR SE COUCHER !")
                            self.joueur_humain.fold()

                            #NOUVELLE MAIN À IMPLEMENTER
                            
                        elif self.bouton_check_rect.collidepoint(event.pos):
                            self.joueur_humain.check()
                            self.dealer.current_player_index = 1
                            self.Flop = True
                            
                        elif self.bouton_raise_rect.collidepoint(event.pos):
                            self.is_raising = True
                            self.raise_input_text = "" 
                            self.input_box_color = self.color_active

                    # Gérer le clic sur la boîte de saisie
                    if self.raise_input_rect.collidepoint(event.pos):
                        self.is_raising = True
                        self.input_box_color = self.color_active
                    elif not self.bouton_raise_rect.collidepoint(event.pos):
                        self.is_raising = False
                        self.input_box_color = self.color_inactive
                        
                    elif event.key == pygame.K_BACKSPACE:
                        # L'utilisateur appuie sur Retour Arrière
                        self.raise_input_text = self.raise_input_text[:-1]
                        
                    else:
                        # On vérifie que c'est bien un chiffre
                        if event.unicode.isdigit():
                            self.raise_input_text += event.unicode



                if self.dealer.game_state == 'postflop' and self.dealer.current_player_index==0:
                        if self.bouton_fold_rect.collidepoint(event.pos):
                            print("CLIC SUR SE COUCHER !")
                            self.joueur_humain.fold()

                            #NOUVELLE MAIN À IMPLEMENTER
                            
                        elif self.bouton_check_rect.collidepoint(event.pos):
                            self.joueur_humain.check()
                            self.dealer.current_player_index = 1
                            
                        elif self.bouton_raise_rect.collidepoint(event.pos):
                            print("CLIC SUR MISER !")
                            # On active le mode saisie !
                            self.is_raising = True
                            self.raise_input_text = "" # On réinitialise le texte
                            self.input_box_color = self.color_active # On change la couleur

                            self.dealer.current_player_index = 1
                            
                        # Pour l'instant on fait toujours commencer le joueur 1 i.e. le héros 
                        # À implémenter plus tard une méthode pour faire commencer l'IA



                if event.type == pygame.KEYDOWN and self.is_raising:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        # L'utilisateur appuie sur ENTRÉE
                        print(f"ACTION: RELANCE VALIDÉE de : {self.raise_input_text}")
                        #
                        # Appelez votre logique de jeu ici avec le montant
                        self.joueur_humain.raise_bet(int(self.raise_input_text))
                        #
                        self.is_raising = False
                        self.input_box_color = self.color_inactive
                        
                    elif event.key == pygame.K_BACKSPACE:
                        # L'utilisateur appuie sur Retour Arrière
                        self.raise_input_text = self.raise_input_text[:-1]
                        
                    else:
                        # On vérifie que c'est bien un chiffre
                        if event.unicode.isdigit():
                            self.raise_input_text += event.unicode
                            
                        
                        



            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()
            
            #Dessin
            self.screen.fill(self.BG_COLOR)
            self.joueur_humain.draw()
            self.joueur_ia.draw()
            self.draw_ui() 
            
            # --- C'est ici que tu dessineras les boutons et le pot ---
            self.draw_ui() # On appelle notre nouvelle fonction de dessin


            if self.Flop == True :
                self.dealer.create_flop()
                for i in range(3):
                        c = self.dealer.reveal_flop()
                        pos = D_POS["flop"][i] # Récupère la position [x, y]
                        c.set_display(screen=self.screen, x=pos[0], y=pos[1], size=120)
                        c.retourner() # On retourne les cartes du joueur

                self.Flop = False

                card.draw() # On dessine la carte communautaire

            # Dessin de la zone de saisie
            if self.is_raising:
                # (Ton code pour dessiner la boîte de saisie est parfait)
                pygame.draw.rect(self.screen, self.input_box_color, self.raise_input_rect, 2)
                text_surface = self.small_font.render(self.raise_input_text, True, (255, 255, 255))
                self.screen.blit(text_surface, (self.raise_input_rect.x + 20, self.raise_input_rect.y + 5))
                label = self.small_font.render("Montant : ", True, (255, 255, 255))
                self.screen.blit(label, (self.raise_input_rect.x - 120, self.raise_input_rect.y + 5))

            pygame.display.update()
            self.clock.tick(self.FPS)

# ... (draw_ui reste la même)

    def draw_ui(self) -> None:
            """Dessine tous les éléments de l'interface (boutons, pot, etc.)."""
            
            pygame.draw.rect(self.screen, (200, 40, 40), self.bouton_fold_rect, border_radius=10)
            texte_surf_fold = self.font_bouton.render('FOLD', True, (255, 255, 255))
            texte_rect_fold = texte_surf_fold.get_rect(center=self.bouton_fold_rect.center)
            self.screen.blit(texte_surf_fold, texte_rect_fold)

            pygame.draw.rect(self.screen, (200, 40, 40), self.bouton_check_rect, border_radius=10)
            texte_surf_check = self.font_bouton.render('CHECK', True, (255, 255, 255))
            texte_rect_check = texte_surf_check.get_rect(center=self.bouton_check_rect.center)
            self.screen.blit(texte_surf_check, texte_rect_check)

            pygame.draw.rect(self.screen, (200, 40, 40), self.bouton_call_rect, border_radius=10)
            texte_surf_call = self.font_bouton.render('CALL', True, (255, 255, 255))
            texte_rect_call = texte_surf_call.get_rect(center=self.bouton_call_rect.center)
            self.screen.blit(texte_surf_call, texte_rect_call)

            pygame.draw.rect(self.screen, (200, 40, 40), self.bouton_raise_rect, border_radius=10)
            texte_surf_raise = self.font_bouton.render('RAISE', True, (255, 255, 255))
            texte_rect_raise= texte_surf_raise.get_rect(center=self.bouton_raise_rect.center)
            self.screen.blit(texte_surf_raise, texte_rect_raise)

            pygame.draw.rect(self.screen, (200, 40, 40), self.bouton_stack1, border_radius=10)
            texte_surf_stack1 = self.font_bouton.render(str(self.joueur_humain._stack), True, (255, 255, 255))
            texte_rect_stack1= texte_surf_stack1.get_rect(center=self.bouton_stack1.center)
            self.screen.blit(texte_surf_stack1, texte_rect_stack1)

            pygame.draw.rect(self.screen, (200, 40, 40), self.bouton_stack2, border_radius=10)
            texte_surf_stack2= self.font_bouton.render(str(self.joueur_ia._stack), True, (255, 255, 255))
            texte_rect_stack2= texte_surf_stack2.get_rect(center=self.bouton_stack2.center)
            self.screen.blit(texte_surf_stack2, texte_rect_stack2)



if __name__ == '__main__':
    game = Game()
    game.run()