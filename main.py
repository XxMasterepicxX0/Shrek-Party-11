import pygame
import sys
from setting import *
from background import BackGround

class Game:
    def __init__(self):
        #initialize all imported pygame modules
        pygame.init()

        # Creates window
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Shrek Party 11")

        self.clock = pygame.time.Clock()
    
    backg_image = BackGround()
    
    # main game loop
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.WIN.fill(COLOR)
            self.backg_image.draw_background()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
