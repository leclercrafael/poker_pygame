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

    def __init__(self,value : int ,color : str, position : int, d_pos : dict, screen: pygame.Surface, size: int ) -> None :
        """Initialize the Object"""
        super().__init__()
        self._screen = screen
        self._x = d_pos[position][0]
        self._y = d_pos[position][1]
        self._size = size     
        self._value = value   
        self._color_name = color.lower()

      
        self.width = self._size
        self.height = self.width * 1.4 


      
        if self._color_name in SUIT_MAP:
            suit_info = SUIT_MAP[self._color_name]
            self.suit_symbol = suit_info["symbol"]
            self.rgb_color = suit_info["color_rgb"]
        else:
           
            self.suit_symbol = "?"
            self.rgb_color = BLACK

       
        try:
           
            font_size_val = int(self.height / 10)
            font_size_suit_small = int(self.height / 9)
            font_size_suit_big = int(self.height / 2.5)
            
            self.font_valeur = pygame.font.SysFont('arial', font_size_val)
            self.font_symbole_petit = pygame.font.SysFont('arial', font_size_suit_small)
            self.font_symbole_grand = pygame.font.SysFont('arial', font_size_suit_big)
        except pygame.error:
            print("Police 'arial' non trouvée, utilisation de la police par défaut.")
            font_size_val = int(self.height / 9)
            font_size_suit_small = int(self.height / 8)
            font_size_suit_big = int(self.height / 2)
            
            self.font_valeur = pygame.font.Font(None, font_size_val)
            self.font_symbole_petit = pygame.font.Font(None, font_size_suit_small)
            self.font_symbole_grand = pygame.font.Font(None, font_size_suit_big)


    @property
    def value(self) -> tuple : 
        """Value of the card"""
        return ((self._value,self._color_name))
    

    def is_background(self) -> bool :
        """Tell if this object is a background object."""
        return False

   


    def draw(self) -> None :
        """Draw the card on screen."""
        """Need to respect the ratio width and height of 1.4"""
        
        
        val_surf = self.font_valeur.render(self._value, True, self.rgb_color)
        suit_small_surf = self.font_symbole_petit.render(self.suit_symbol, True, self.rgb_color)
        suit_big_surf = self.font_symbole_grand.render(self.suit_symbol, True, self.rgb_color)
        
   
        card_rect = pygame.Rect(self._x, self._y, self.width, self.height)
        

        pygame.draw.rect(self._screen, WHITE, card_rect, border_radius=int(self.width * 0.07)) 

        pygame.draw.rect(self._screen, BLACK, card_rect, 2, border_radius=int(self.width * 0.07))
        
     
        padding_x = self.width * 0.05 
        padding_y = self.height * 0.02


        self._screen.blit(val_surf, (self._x + padding_x, self._y + padding_y))
        self._screen.blit(suit_small_surf, (self._x + padding_x, self._y + padding_y + val_surf.get_height()*0.9))


        center_rect = suit_big_surf.get_rect(
            center=(self._x + self.width / 2, self._y + self.height / 2)
        )
        self._screen.blit(suit_big_surf, center_rect)


        val_roto = pygame.transform.rotate(val_surf, 180)
        suit_roto = pygame.transform.rotate(suit_small_surf, 180)
        
        self._screen.blit(val_roto, (self._x + self.width - val_roto.get_width() - padding_x, 
                                    self._y + self.height - val_roto.get_height() - padding_y))
        self._screen.blit(suit_roto, (self._x + self.width - suit_roto.get_width() - padding_x, 
                                    self._y + self.height - suit_roto.get_height() - padding_y - val_roto.get_height()*0.9))

