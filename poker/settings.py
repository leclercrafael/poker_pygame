class Settings():
  
  def __init__(self) -> None :
    self.TITLE_STRING = 'Poker Game'
    self.FPS = 120
    self.HEIGHT = 1080
    self.WIDTH = 1920
    self.BG_COLOR = (33, 124, 66)
    self.GAME_FONT = 'graphics/PixelatedDisplay.ttf'
    HEIGHT = 100
    # Position of the cards. They are hard-coded, not the best when we will have more than 2 players

    self.P1_C1 = (20, (HEIGHT/2))
    self.P1_C2 = (80, (HEIGHT/2))

    self.P2_C1 = (1900, (HEIGHT/2))
    self.P2_C2 = (1920, (HEIGHT/2))

    self.SMALL_BLIND = 10
    self.BIG_BLIND = 20


    self.value_dict = {
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

    self.VALEURS = [i for i in range(2,15)]
    self.COULEURS = ['Coeur', 'Pique', 'Carreau', 'Trèfle']


    self.d_pos = { "1" : [50,100], "2" : [110,100]}
