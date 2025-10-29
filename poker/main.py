from .settings import Settings
import ctypes, pygame, sys
from .card import Card

d_pos = { "1" : [50,100], "2" : [110,100]}

__name__ = "__main__"

class Game(Settings):
    def __init__(self):
        super().__init__()
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption(self.TITLE_STRING)
        self.clock = pygame.time.Clock()

        self.card1 = Card(
                screen=self.screen, 
                d_pos=d_pos, 
                position='1', 
                size=100,         
                value="10", 
                color="pique" # Chaîne
                )
        self.card2 = Card(
                screen=self.screen, 
                d_pos=d_pos, 
                position='2', 
                size=100,         
                value="6", 
                color="coeur" # Chaîne
                )
        self.SPACE = False
        #self.hand = Hand()


    def run(self):

        self.start_time = pygame.time.get_ticks()

        while True:
            # Handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_down = True

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if mouse_down :  
                            mouse_down = False
                            #self.hand = Hand()
                if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    self.SPACE = True
                
                    

            # Time variables
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()
            pygame.display.update()
            self.screen.fill(self.BG_COLOR)
            if self.SPACE :
                    self.card1.draw()
                    self.card2.draw()
            #self.hand.update()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    game = Game()
    game.run()


