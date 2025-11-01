# Fichier main.py

from settings import Settings
import ctypes, pygame, sys
# from card import Card # Plus besoin d'importer Card ici
# from deck import Deck # Plus besoin d'importer Deck ici
from dealer import Dealer
from player import Player # <-- AJOUTER L'IMPORT DU JOUEUR

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

        # On garde la logique de la touche ESPACE
        self.SPACE = False 

    def run(self):
        self.start_time = pygame.time.get_ticks()

        while True:
            # --- 1. GESTION DES ÉVÉNEMENTS ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.SPACE = True
            
            # --- 2. GESTION DU TEMPS ---
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()
            
            # --- 3. LOGIQUE DE DESSIN ---
            
            # Étape A: EFFACER
            self.screen.fill(self.BG_COLOR)
            
            # Étape B: DESSINER
            if self.SPACE:
                # On demande aux JOUEURS de se dessiner
                self.joueur_humain.draw()
                self.joueur_ia.draw()
                
                # Plus tard, on ajoutera :
                # self.dealer.draw() # Pour dessiner le pot, le flop, etc.
            
            # Étape C: MONTRER
            pygame.display.update()
            
            # --- 4. CONTRÔLE DU FPS ---
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    game = Game()
    game.run()