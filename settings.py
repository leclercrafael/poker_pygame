TITLE_STRING = 'Poker Game'
FPS = 120
HEIGHT = 1080
WIDTH = 1920
BG_COLOR = (33, 124, 66)
GAME_FONT = 'graphics/PixelatedDisplay.ttf'

# Position of the cards. They are hard-coded, not the best when we will have more than 2 players

P1_C1 = (20, (HEIGHT/2))
P1_C2 = (80, (HEIGHT/2))

P2_C1 = (1900, (HEIGHT/2))
P2_C2 = (1920, (HEIGHT/2))


value_dict = {
  'T': 10,
  'J': 11,
  'Q': 12,
  'K': 13,
  'A': 14,
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9
}

VALEURS = [i for i in range(2,15)]
COULEURS = ['Coeur', 'Pique', 'Carreau', 'Trèfle']
