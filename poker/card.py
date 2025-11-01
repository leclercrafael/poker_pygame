from game_object import GameObject
import typing
import pygame
import sys
from settings import Settings

# --- Définitions globales ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Dictionnaire de mappage pour les couleurs/symboles
SUIT_MAP = {
    "coeur":   {"symbol": "♥", "color_rgb": RED},
    "carreau": {"symbol": "♦", "color_rgb": RED},
    "pique":   {"symbol": "♠", "color_rgb": BLACK},
    "trefle":  {"symbol": "♣", "color_rgb": BLACK}
}


class Card(GameObject) :

    def __init__(self, value : int, color : str) -> None :
        """Initialize the Object"""
        super().__init__()  
        self._value = value   
        self._color_name = color.lower()
        self.est_retournee = False

      
        if self._color_name in SUIT_MAP:
            suit_info = SUIT_MAP[self._color_name]
            self.suit_symbol = suit_info["symbol"]
            self.rgb_color = suit_info["color_rgb"]
        else:
            self.suit_symbol = "?"
            self.rgb_color = BLACK

        self._screen = None
        self._x = 0
        self._y = 0
        self.width = 70
        self.height = 98 
        self.font_valeur = None
        self.font_symbole_petit = None
        self.font_symbole_grand = None
        self.rect = pygame.Rect(self._x, self._y, self.width, self.height) # Création d'un rect

       
    def set_display(self, screen: pygame.Surface, x: int, y: int, size: int):
        """Configure les attributs Pygame (écran, position, taille, polices)."""
        self._screen = screen
        self._x = x
        self._y = y
        self.width = size
        self.height = size * 1.4 # Maintient le ratio
        self.rect = pygame.Rect(self._x, self._y, self.width, self.height)
        
        # --- Chargement/Calcul des Polices (Déplacé ici) ---
        try:
            # Polices proportionnelles à la nouvelle taille
            font_size_val = int(self.height / 10)
            font_size_suit_small = int(self.height / 9)
            font_size_suit_big = int(self.height / 2.5)
            
            self.font_valeur = pygame.font.SysFont('arial', font_size_val)
            self.font_symbole_petit = pygame.font.SysFont('arial', font_size_suit_small)
            self.font_symbole_grand = pygame.font.SysFont('arial', font_size_suit_big)

        except pygame.error:
            # Gestion d'erreur (si la police n'est pas trouvée)
            font_size_val = int(self.height / 9)
            font_size_suit_small = int(self.height / 8)
            font_size_suit_big = int(self.height / 2)
            
            self.font_valeur = pygame.font.Font(None, font_size_val)
            self.font_symbole_petit = pygame.font.Font(None, font_size_suit_small)
            self.font_symbole_grand = pygame.font.Font(None, font_size_suit_big)


    @property
    def value(self) -> tuple : 
        """Valeur de la carte (getter)."""
        return (self._value, self._color_name)
    
    def retourner(self) -> None:
        """Bascule l'état visible/caché de la carte."""
        self.est_retournee = not self.est_retournee


    def is_background(self) -> bool :
        """Indique si l'objet est un élément de fond."""
        return False

    # 3. La méthode draw() est légèrement modifiée pour gérer l'état
    def draw(self) -> None :
        """Dessine la carte sur l'écran (face ou dos)."""
        
        # Vérification essentielle : La carte doit être configurée
        if not self._screen or not self.font_valeur:
            print(f"Erreur : La carte {self._value} de {self._color_name} n'est pas configurée pour l'affichage (set_display non appelé).")
            return
            
        card_rect = self.rect # Utilise le rect mis à jour par set_display ou par défaut

        if not self.est_retournee:
            # --- Dessin du DOS de la carte (Simplifié) ---
            # Dessine un rectangle vert/bleu pour simuler le dos
            pygame.draw.rect(self._screen, (0, 0, 150), card_rect, border_radius=int(self.width * 0.07))
            
            # Optionnel : Ajouter un logo ou un texte "Poker" pour le dos
            font_dos = pygame.font.Font(None, int(self.height / 4))
            dos_surf = font_dos.render("Poker", True, WHITE)
            dos_rect = dos_surf.get_rect(center=card_rect.center)
            self._screen.blit(dos_surf, dos_rect)
            
        else:
            # --- Dessin de la FACE de la carte (Ton code original) ---
            
            val_surf = self.font_valeur.render(self._value, True, self.rgb_color)
            suit_small_surf = self.font_symbole_petit.render(self.suit_symbol, True, self.rgb_color)
            suit_big_surf = self.font_symbole_grand.render(self.suit_symbol, True, self.rgb_color)
        
            pygame.draw.rect(self._screen, WHITE, card_rect, border_radius=int(self.width * 0.07)) 
            pygame.draw.rect(self._screen, BLACK, card_rect, 2, border_radius=int(self.width * 0.07))
            
            padding_x = self.width * 0.05 
            padding_y = self.height * 0.02

            # Coin supérieur gauche
            self._screen.blit(val_surf, (self._x + padding_x, self._y + padding_y))
            self._screen.blit(suit_small_surf, (self._x + padding_x, self._y + padding_y + val_surf.get_height()*0.9))

            # Centre
            center_rect = suit_big_surf.get_rect(
                center=(self._x + self.width / 2, self._y + self.height / 2)
            )
            self._screen.blit(suit_big_surf, center_rect)

            # Coin inférieur droit (rotation)
            val_roto = pygame.transform.rotate(val_surf, 180)
            suit_roto = pygame.transform.rotate(suit_small_surf, 180)
            
            self._screen.blit(val_roto, (self._x + self.width - val_roto.get_width() - padding_x, 
                                        self._y + self.height - val_roto.get_height() - padding_y))
            self._screen.blit(suit_roto, (self._x + self.width - suit_roto.get_width() - padding_x, 
                                        self._y + self.height - suit_roto.get_height() - padding_y - val_roto.get_height()*0.9))