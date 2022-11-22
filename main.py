import pygame
import sys
from setting import *
from player import Player_CLASS

players = Player_CLASS(1, 200, 310)



class Game:
    def __init__(self):

        pygame.init()

        # Creates window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Shrek Party 11")

        self.clock = pygame.time.Clock()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(COLOR)
            self.screen.blit(CHARACTER, (self.player.x,self.player.y))
            pygame.display.update()
            self.clock.tick(FPS)
    
    key_pressed = pygame.key.get_pressed()
    players.movement(key_pressed, players)


if __name__ == '__main__':
    game = Game()
    game.run()
