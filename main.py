import pygame
import sys
from setting import *
from player import Player_CLASS




players = Player_CLASS(1, 200, 310)

class Game:
    def __init__(self):

        pygame.init()

        # Creates window
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Shrek Party 11")

        self.clock = pygame.time.Clock()
        
    def draw_window(self, players):
            self.WIN.fill(COLOR)
            self.WIN.blit(CHARACTER, (players.x,players.y))
            pygame.display.update()

    def run(self):
        player = pygame.Rect(self.x, self.y, C_WIDTH, C_HEIGHT )

        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            key_pressed = pygame.key.get_pressed()
            #players.movement(key_pressed, players)

            self.draw_window(players)

if __name__ == '__main__':
    game = Game()
    game.run()
