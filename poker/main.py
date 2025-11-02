# Fichier main.py

from .settings import Settings
import ctypes, pygame, sys
# from card import Card # Plus besoin d'importer Card ici
# from deck import Deck # Plus besoin d'importer Deck ici
from .dealer import Dealer
from .player import Player # <-- AJOUTER L'IMPORT DU JOUEUR

# Dictionnaire des positions pour les mains
# On le rend plus descriptif
D_POS = {
    # Positions (x, y) pour les 2 cartes du joueur humain
    "joueur_main": [[50, 500], [180, 500]], 
    # Positions (x, y) pour les 2 cartes de l'IA
    "ia_main": [[50, 100], [180, 100]],
}

__name__ = "__main__"

class Game(Settings):
    def __init__(self):
        super().__init__()
        # Initialisation générale de Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption(self.TITLE_STRING)
        self.clock = pygame.time.Clock()
        
        # --- Création des objets de jeu ---
        self.dealer = Dealer()
        
        # Création des joueurs
        self.joueur_humain = Player(name="Héros", stack=1000, is_ia=False)
        self.joueur_ia = Player(name="IA", stack=1000, is_ia=True)
        
        # Le Dealer connaît ses joueurs
        self.dealer.add_player(self.joueur_humain)
        self.dealer.add_player(self.joueur_ia)

        # --- Lancement de la première main ---
        self.dealer.nouvelle_main() # Prépare le deck et les joueurs
        self.dealer.draw_new_hand() # Distribue 2 cartes logiques
        
        # --- Configuration de l'affichage des cartes distribuées ---
        # C'est l'étape clé : on dit aux cartes où se dessiner
        
        # 1. Cartes du Joueur Humain
        for i, card in enumerate(self.joueur_humain.main):
            pos = D_POS["joueur_main"][i] # Récupère la position [x, y]
            card.set_display(screen=self.screen, x=pos[0], y=pos[1], size=120)
            card.retourner() # On retourne les cartes du joueur

        # 2. Cartes de l'IA
        for i, card in enumerate(self.joueur_ia.main):
            pos = D_POS["ia_main"][i]
            card.set_display(screen=self.screen, x=pos[0], y=pos[1], size=120)
            # On ne les retourne PAS ! Elles s'afficheront face cachée.


        #UI

        self.bouton_fold_rect = pygame.Rect(500, 800, 200, 70)
        self.bouton_check_rect = pygame.Rect(750, 800, 200, 70)
        self.bouton_call_rect = pygame.Rect(1000, 800, 200, 70)
        self.bouton_raise_rect = pygame.Rect(1250, 800, 200, 70)


# --- Variables pour la saisie de la relance ---
        self.is_raising = False      # État : sommes-nous en train de saisir une relance ?
        self.raise_input_text = ""   # Le texte en cours de saisie
        # Un rectangle pour la zone de saisie
        self.raise_input_rect = pygame.Rect(300, 450, 140, 40) 
        self.color_active = pygame.Color('dodgerblue2')
        self.color_inactive = pygame.Color('lightgray')
        self.input_box_color = self.color_inactive


        try:
            # Assure-toi que cette ligne est présente !
            self.font_bouton = pygame.font.SysFont('arial', 30, bold=True)
        except pygame.error:
            self.font_bouton = pygame.font.Font(None, 36)


    def run(self):
        self.start_time = pygame.time.get_ticks()

        while True:
            # --- 1. GESTION DES ÉVÉNEMENTS ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.dealer.game_state == 'preflop' and self.dealer.current_player_index==0:
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
                        # self.player_raise(int(self.raise_input_text))
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
                            
                        
                        


            
            # --- 2. GESTION DU TEMPS ---
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()
            
# --- 4. LOGIQUE DE DESSIN ---
            
            # Étape A: EFFACER
            self.screen.fill(self.BG_COLOR)
            
            # Étape B: DESSINER
            self.joueur_humain.draw()
            self.joueur_ia.draw()
            
            # --- C'est ici que tu dessineras les boutons et le pot ---
            self.draw_ui() # On appelle notre nouvelle fonction de dessin

            # --- Dessin de la zone de saisie ---
            if self.is_raising:
                # Dessine la boîte de saisie
                pygame.draw.rect(self.screen, self.input_box_color, self.raise_input_rect, 2) # Juste le contour
                
                # Prépare le texte à afficher
                text_surface = self.small_font.render(self.raise_input_text, True, (255, 255, 255))
                
                # Affiche le texte (avec un petit padding)
                self.screen.blit(text_surface, (self.raise_input_rect.x + 5, self.raise_input_rect.y + 5))
                
                # (Optionnel) Affiche un label
                label = self.small_font.render("Montant:", True, (255, 255, 255))
                self.screen.blit(label, (self.raise_input_rect.x - 80, self.raise_input_rect.y + 5))
            
            # Étape C: MONTRER
            pygame.display.update()
            
            # --- 5. CONTRÔLE DU FPS ---
            self.clock.tick(self.FPS)


    def draw_ui(self):
            """Dessine tous les éléments de l'interface (boutons, pot, etc.)."""
            
            # --- Dessin du bouton SE COUCHER ---
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

            # --- (Plus tard, tu ajouteras les boutons CHECK et RAISE ici) ---

if __name__ == '__main__':
    game = Game()
    game.run()